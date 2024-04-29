from rest_framework import serializers
from .models import User, Role, Permission
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        def validate_phone_number(self, phone_number):
            number_format = re.compile(r'^\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$')

            if not number_format.match(phone_number):
                raise serializers.ValidationError("Phone number formati xato")
            return phone_number


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Role
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'
