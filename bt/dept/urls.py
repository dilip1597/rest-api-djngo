from django.urls import path , include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


router = routers.DefaultRouter()
router.register(r'deparment',DepartmentViewSet )
urlpatterns = [
    path('', include(router.urls)),
    ]