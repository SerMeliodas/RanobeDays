from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from apps.common.models import BaseModel


class Comment(BaseModel):
    TYPES = (
        ('novel', 'Novel'),
        ('chapter', 'Chapter')
    )

    comment_type = models.CharField(max_length=10, choices=TYPES)
    message = models.TextField()
    user = models.ForeignKey(get_user_model(), related_name='comments',
                             on_delete=models.CASCADE)
    novel = models.ForeignKey('novels.Novel', null=True, blank=True,
                              on_delete=models.CASCADE)
    chapter = models.ForeignKey('chapters.Chapter', null=True, blank=True,
                                on_delete=models.CASCADE)

    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='child')

    def clean(self, *args, **kwargs):
        if (self.novel is None) and (self.chapter is None):
            raise ValidationError('One field must be set Novel or Chapter')

        return super().clean(*args, **kwargs)

    class Meta:
        db_table = 'comments'
        constraints = [
            models.CheckConstraint(
                check=models.Q(novel=None, chapter__isnull=False) |
                models.Q(chapter=None, novel__isnull=False),
                name='One of the to not null'
            )
        ]
