
from django.db.models import fields
from rest_framework import serializers
from .models import  Emp
 




class EmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emp
        fields = ( 'id','name','phone','email','address')                


