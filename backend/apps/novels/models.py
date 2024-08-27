from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

from PIL import Image


def _get_image_save_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"novel_covers/{instance.title}.{extension}"


class Novel(BaseModel):
    STATUS = (
        ('continues', _("Continues")),
        ('finished', _("Finished")),
        ('frozen', _("Frozen")),
        ('licensed', _("Licensed"))
    )

    title = models.CharField(max_length=255, unique=True)

    cover = models.ImageField(default="default_novel_cover.png",
                              upload_to=_get_image_save_path)

    creator = models.ForeignKey("teams.Team", on_delete=models.DO_NOTHING,
                                related_name="created_novels", default=None)

    slug = models.SlugField(max_length=255, default=title, db_index=True)
    original_title = models.CharField(max_length=255, null=True, blank=True)
    language = models.ForeignKey("metadata.Language", db_index=True,
                                 on_delete=models.DO_NOTHING,
                                 related_name="novels",
                                 default=None)
    translated_language = models.ForeignKey("metadata.Language",
                                            db_index=True,
                                            on_delete=models.DO_NOTHING,
                                            related_name="translated_novels",
                                            null=True)
    country = models.ForeignKey("metadata.Country", db_index=True,
                                on_delete=models.DO_NOTHING,
                                default=None)
    status = models.CharField(choices=STATUS, default=STATUS[0][0])
    tags = models.ManyToManyField("metadata.Tag", db_index=True)
    genres = models.ManyToManyField("metadata.Genre", db_index=True)
    synopsys = models.TextField(null=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "novels"

    def _resize_cover(self):
        cover = Image.open(self.cover.path)
        output_size = (600, 800)
        if cover.width != output_size[0] or cover.height != output_size[1]:
            cover = cover.resize(
                size=output_size, resample=Image.Resampling.LANCZOS
            )
            cover.save(self.cover.path)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if kwargs.get("update_fields"):
            kwargs["update_fields"].append("slug")

        super().save(*args, **kwargs)

        self._resize_cover()

    def __str__(self):
        return f"{self.title} - {self.status}"
