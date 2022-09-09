from rest_framework.response import Response
from imp import source_from_cache
from django.db.models import fields
from rest_framework import serializers
from .models import  SoftwareType, SoftwreSubType, Software, ComputerSoftwareType
 
from django.contrib.auth.models import User 





class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ('id','username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    
















class SoftwareTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoftwareType
        fields = ( 'id','name','discription','created_by','updated_by','created_on','updated_on','is_active') 
        
        def to_representation(self, instance):
         row = super(SoftwareTypeSerializer, self).to_representation(instance)
         return {row["name"]:row}

                       




class SoftwreSubtypeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = SoftwreSubType
        fields = ( 'id','software_type','name','discription','created_by','updated_by','created_on','updated_on','is_active')                


class SoftwareSerializer(serializers.ModelSerializer):

    class Meta:
        model = Software
        fields = ( 'id','software_sub_type','computer_software_type','name','version','port_numbers','sub_types','discription','created_by','updated_by','created_on','updated_on','is_active') 


class ComputerSoftwareTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ComputerSoftwareType
        fields = ( 'id','name','discription','created_by','updated_by','created_on','updated_on','is_active')                


