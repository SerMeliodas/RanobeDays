from rest_framework.pagination import LimitOffsetPagination as _LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings


class LimitOffsetPagination(_LimitOffsetPagination):
    max_limit = 50

    def get_paginated_data(self, data):
        return {
            'limit': self.limit,
            'offset': self.offset,
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        }

    def get_paginated_response(self, data):
        return Response({
            'limit': self.limit,
            'offset': self.offset,
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'data': data
        })


def get_paginated_response(*, pagination_class=None, serializer_class,
                           queryset, request, view):
    if pagination_class:
        paginator = pagination_class()
    else:
        paginator = api_settings.DEFAULT_PAGINATION_CLASS()

    page = paginator.paginate_queryset(queryset, request, view=view)

    if page is not None:
        serializer = serializer_class(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    serializer = serializer_class(queryset, many=True)
    return Response(data=serializer.data)
