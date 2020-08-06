from src.applicationlayer.breeds.serializers import BreedSerializer
from src.entities import models
from rest_framework import viewsets, status, permissions


class BreedViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = BreedSerializer
    queryset = models.Breed.objects.all()
