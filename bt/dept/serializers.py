
from django.db.models import fields
from rest_framework import serializers
from .models import Department
 




class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ( 'id','name','parent','uuid','created_by','updated_by','created_on','updated_on','is_active')                


