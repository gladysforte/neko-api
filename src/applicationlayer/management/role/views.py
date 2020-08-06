from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from src.applicationlayer.management.role.serializers import RoleSerializer
from src.entities import models
from src.utilities.utils import CustomResponse
# Create your views here.

class RoleViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = RoleSerializer
    queryset = models.Role.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = models.Role.objects.filter(is_active=True)
        return CustomResponse.response(self, queryset)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response({
                'message': 'Successfully archived'
            },
            status=status.HTTP_200_OK
        )

