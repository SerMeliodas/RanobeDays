from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Novel(BaseModel):
    STATUS = (
        (1, _("Continues")),
        (2, _("Finished")),
        (3, _("Frozen"))
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=title, db_index=True)
    original_title = models.CharField(max_length=255, null=True)
    language = models.ForeignKey("metadata.Language", db_index=True,
                                 on_delete=models.DO_NOTHING,
                                 related_name="novels",
                                 default=None)
    translate_language = models.ForeignKey("metadata.Language",
                                           db_index=True,
                                           on_delete=models.DO_NOTHING,
                                           related_name="translated_novels",
                                           null=True)
    country = models.ForeignKey("metadata.Country", db_index=True,
                                on_delete=models.DO_NOTHING,
                                default=None)
    status = models.IntegerField(choices=STATUS, default=1)
    tags = models.ManyToManyField("metadata.Tag", db_index=True)
    genres = models.ManyToManyField("metadata.Genre", db_index=True)
    synopsys = models.TextField(null=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "novels"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if kwargs.get("update_fields"):
            kwargs["update_fields"].append("slug")

        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {Novel.STATUS[self.status - 1][1]}"
