from .models import Team
from django.db.models import QuerySet
import django_filters


class TeamFilter(django_filters.FilterSet):
    users = django_filters.BaseInFilter(
        field_name='users__pk', lookup_expr='in')
    novels = django_filters.BaseInFilter(
        field_name='novels__pk', lookup_expr='in')
    team_type = django_filters.ChoiceFilter(choices=Team.TEAM_TYPES)

    class Meta:
        model = Team
        fields = ['users', 'novels', 'team_type']


def get_teams(*, filters=None) -> QuerySet:
    filters = filters or {}

    qs = Team.objects.all()
    filter = TeamFilter(filters, queryset=qs)

    return filter.qs


def get_team(pk: int) -> Team:
    return Team.objects.get(pk=pk)
