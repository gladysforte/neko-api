from django.db import transaction
from rest_framework import serializers
from src.applicationlayer.management.permission.serializers import PublicPermissionSerializer
from src.entities.models import Role, Permission


class PublicRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['label', 'name']

class RoleSerializer(serializers.ModelSerializer):

    permissions = serializers.SerializerMethodField()
    class Meta:
        model = Role
        fields = ['id', 'label', 'name', 'permissions']
    
    def get_permissions(self, obj):
        _obj = PublicPermissionSerializer(obj.permissions, many=True)
        return _obj.data

    def create(self, validated_data):
        request = self.context['request']
        name = validated_data['name']
        label = validated_data['label']
        permissions = request.data['permissions']
        role = Role(name=name, label=label, is_active=True)
        role.save()
        err_permission = None
        try:
            with transaction.atomic():
                for perm_id in permissions:
                    err_permission = perm_id
                    _perm = Permission.objects.get(id=perm_id)
                    role.permissions.add(_perm)
        except:
            role.delete()
            raise serializers.ValidationError({
                "permissions": [
                    'Permission with id of {} is invalid.'.format(err_permission)
                ]
            })
        return role

    def update(self, instance, validated_data):
        request = self.context['request']
        name = validated_data['name']
        label = validated_data['label']
        permissions = request.data['permissions']
        role = instance
        role.name = name
        role.label = label
        if 'is_active' in validated_data:
            role.is_active = validated_data['is_active']
        else:
            role.is_active = True
        err_permission = None
        try:
            with transaction.atomic():
                role.permissions.clear()
                for perm_id in permissions:
                    err_permission = perm_id
                    _perm = Permission.objects.get(id=perm_id)
                    role.permissions.add(_perm)
                role.save()
        except:
            raise serializers.ValidationError({
                "permissions": [
                    'Permission with id of {} is invalid.'.format(err_permission)
                ]
            })
        return role

