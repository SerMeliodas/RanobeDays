from .models import Comment
from django.db.models import QuerySet
import django_filters


class CommentFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(field_name='user__username')
    novel = django_filters.CharFilter(field_name='novel__slug')
    chapter = django_filters.NumberFilter(field_name='chapter__pk')

    class Meta:
        model = Comment
        fields = ('user', 'novel', 'chapter')


def get_comments(*, filters: dict | None = None) -> QuerySet[Comment]:
    filters = filters or {}

    qs = Comment.objects.all()
    filter = CommentFilter(filters, qs)

    return filter.qs


def get_comment(pk: int) -> Comment:
    return Comment.objects.get(pk=pk)
