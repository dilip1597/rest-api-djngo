from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import *
from .import views



router = routers.DefaultRouter()
# router.register(r'bottles', views.BottleViewSet, base_name='bottles')
router.register(r'Softwaretype', SoftwareTypeViewSet)
router.register(r'SoftwreSubType', SoftwreSubtypeViewSet)
router.register(r'Software', SoftwareViewSet)
router.register(r'ComputerSoftwareType', ComputerSoftwareTypeViewSet)
router.register(r'user', UserCreateViewSet)

 


urlpatterns = [
      
         path('', include(router.urls)),
         path('api-auth/', include('rest_framework.urls')),
         path('hello/', views.HelloView.as_view(), name ='hello'),
         # path('register', views.UserCreate.as_view()),
    #    path('softwaresubtype/', views.SoftwreSubtypeList.as_view(),name='softwaresubtype'),
    #    path('softwaresubtype/<int:pk>/', views.SoftwreSubtypeDetail.as_view(),name='softwaresubtype'),

      
    #    path('computersoftwaretype/', views.ComputerSoftwareTypeList.as_view(),name='computersoftwaretype'),
    #    path('computersoftwaretype/<int:pk>/', views.ComputerSoftwareTypeDetail.as_view(),name='computersoftwaretype'),
    #    path('software/', views.SoftwareList.as_view(),name='software'),
    #    path('software/<int:pk>/', views.SoftwareDetail.as_view(),name='software'),
 ] 

    
