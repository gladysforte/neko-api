from rest_framework import viewsets, permissions

from src.applicationlayer.management.permission.serializers import PermissionSerializer
from src.entities import models
# Create your views here.

class PermissionViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = PermissionSerializer
    queryset = models.Permission.objects.all()
