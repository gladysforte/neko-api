from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from src.applicationlayer.management.permission import views as permission
from src.applicationlayer.management.role import views as role
from src.applicationlayer.breeds import views as breed

router = DefaultRouter()
router.register(r'permission', permission.PermissionViewSet)
router.register(r'role', role.RoleViewSet)
router.register(r'breeds', breed.BreedViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
