from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model

from src.accesslayer import serializers

User = get_user_model()
class UserRegistrationViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


    