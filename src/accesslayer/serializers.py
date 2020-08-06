from rest_framework import serializers
from django.contrib.auth import get_user_model

from src.applicationlayer.management.role.serializers import PublicRoleSerializer

from src.entities import models

User = get_user_model()
class UserRegistrationSerializer(serializers.ModelSerializer):

    roles = PublicRoleSerializer(many=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'roles'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        request = self.context['request']
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        roles = request.data['roles']
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        err_role = None #the role that will cause error
        try:
            for role in roles:
                err_role = role
                _role = models.Role.objects.get(id=role['id'])
                user.roles.add(_role)
        except:
            user.delete()
            raise serializers.ValidationError({
                "roles": ['Role with id of {} is invalid.'.format(err_role['id'])]
            })
        return user
        