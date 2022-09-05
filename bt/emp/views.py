from rest_framework import generics
from .models import Emp
from .serializers import EmpSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
  
  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)


class EmpList(generics.ListCreateAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer


class EmpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer



