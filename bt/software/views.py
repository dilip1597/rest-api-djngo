from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.contrib.auth.models import User 
# Create your views here.


from rest_framework import generics

from .models import SoftwareType,SoftwreSubType,Software,ComputerSoftwareType
from .serializers import UserSerializer,SoftwareTypeSerializer,SoftwreSubtypeSerializer,SoftwareSerializer,SoftwareTypeSerializer,ComputerSoftwareTypeSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
  
  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)




class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {obj['id']: obj for obj in serializer.data}
        return Response({'Users': data})

    




class SoftwareTypeViewSet(viewsets.ModelViewSet):
    queryset = SoftwareType.objects.all()
    serializer_class = SoftwareTypeSerializer
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {obj['id']: obj for obj in serializer.data}
        return Response({'Softwaretype': data})


class SoftwreSubtypeViewSet(viewsets.ModelViewSet):
    queryset = SoftwreSubType.objects.all()
    serializer_class = SoftwreSubtypeSerializer




class SoftwareViewSet(viewsets.ModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = {obj['id']: obj for obj in serializer.data}
        return Response({'Software': data})


class ComputerSoftwareTypeViewSet(viewsets.ModelViewSet):
    queryset = ComputerSoftwareType.objects.all()
    serializer_class = ComputerSoftwareTypeSerializer


