
# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Service, Customerinfo, Emp
 
# Create a model serializer
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Service
        fields = ('id','name','price')


class CustomerinfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customerinfo
        fields = ('id','name','phone','email','address')




class EmpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emp
        fields = ('name','phone','email','address','user')