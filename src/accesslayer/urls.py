from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework.routers import DefaultRouter

from src.accesslayer import views

router = DefaultRouter()
router.register(r'', views.UserRegistrationViewSet)


urlpatterns = [
    path('register/', include(router.urls)),
    path('login/', obtain_jwt_token, name='login'),
    path('refresh/', refresh_jwt_token, name='refresh'),
    path('verify/', verify_jwt_token, name='verify'),
]
