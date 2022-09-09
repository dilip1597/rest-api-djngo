
from django.db.models import fields
from rest_framework import serializers
from .models import Department
 
from django.contrib.auth.models import User



class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ( 'id','name','parent','uuid','created_by','updated_by','created_on','updated_on','is_active')                


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
