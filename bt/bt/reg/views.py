# import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import local data
from .serializers import ServiceSerializer,CustomerinfoSerializer,EmpSerializer
from .models import Service, Customerinfo, Emp

 
# create a viewset
class  ServiceViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Service.objects.all()
     
    # specify serializer to be used
    serializer_class = ServiceSerializer

class CustomerinfoViewSet(viewsets.ModelViewSet):
    queryset = Customerinfo.objects.all()
    serializer_class =CustomerinfoSerializer





class EmpApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # def get(self, request, *args, **kwargs):
    #     '''
    #     List all the todo items for given requested user
    #     '''
    #     test = Emp.objects.filter(user = request.user.id)
    #     serializer = EmpSerializer(test, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by Category': '/?category=category_name',
#         'Search by Subcategory': '/?subcategory=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }
  
#     return Response(api_urls)   
# 
#  
def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name'), 
            'phone': request.data.get('phone'), 
            'email': request.data.get('emile'),
            'address': request.data.get('address'),
            'user': request.user.id
        }
        serializer = EmpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)