from django.contrib import admin
from django.contrib.auth import get_user_model
from src.entities.models import User, Role, Permission

admin.site.register(Role)
admin.site.register(Permission)

# @admin.register(User)
# class CustomUserAdmin(admin.ModelAdmin):
#     pass