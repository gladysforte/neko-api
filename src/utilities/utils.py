from rest_framework.response import Response

class CustomResponse:

    @staticmethod
    def response(paginator, queryset):
        page = paginator.paginate_queryset(queryset)
        if page is not None:
            serializer = paginator.get_serializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = paginator.get_serializer(queryset, many=True)
            return Response(serializer.data)