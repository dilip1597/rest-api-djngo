"""bt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # new
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt import views as jwt_views

# from django.views.generic import TemplateView


urlpatterns = [	
    # path('openapi/', get_schema_view(
    #     title="Binary Hat",
    #     description="API for developers who would love to use our service in a Binary Hat" 
    # ), name='openapi-schema'),
    # path('docs/', TemplateView.as_view(
    #     template_name='documentation.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
   

    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path('admin/', admin.site.urls),
    path('emp/', include('emp.urls')),
    path('dept/', include('dept.urls')),# new
    path('', include('software.urls',)),
      
    


    # path('ComputerSoftwareType/', include('software.urls')),
]