from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework import generics 

from .models import SoftwareType,SoftwreSubType,Software,ComputerSoftwareType
from .serializers import SoftwareTypeSerializer,SoftwreSubtypeSerializer,SoftwareSerializer,SoftwareTypeSerializer,ComputerSoftwareTypeSerializer




class SoftwareTypeViewSet(viewsets.ModelViewSet):
    queryset = SoftwareType.objects.all()
    serializer_class = SoftwareTypeSerializer




class SoftwreSubtypeViewSet(viewsets.ModelViewSet):
    queryset = SoftwreSubType.objects.all()
    serializer_class = SoftwreSubtypeSerializer




class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer




class ComputerSoftwareTypeViewSet(viewsets.ModelViewSet):
    queryset = ComputerSoftwareType.objects.all()
    serializer_class = ComputerSoftwareTypeSerializer


