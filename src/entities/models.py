from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Permission(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'permission'

    def __str__(self):
        return self.label


class Role(models.Model):

    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    permissions = models.ManyToManyField(Permission, related_name='role')
    
    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.label


class User(AbstractUser):
    roles = models.ManyToManyField(Role, related_name='user')

    class Meta:
        db_table = 'user'


class Breed(models.Model):

    name = models.CharField(max_length=255)
    alternative_name = models.CharField(max_length=255, null=True)
    origin = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    lifespan = models.CharField(max_length=255, null=True)
    picture = models.ImageField(upload_to='images/', null=True,
                            max_length=255)

    class Meta:
        db_table = 'breeds'
