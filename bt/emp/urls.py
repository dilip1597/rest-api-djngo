from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from emp import views



  
urlpatterns = [
    path('hello/', views.HelloView.as_view(), name ='hello'),
    path('', views.EmpList.as_view()),
    path('<int:pk>/', views.EmpDetail.as_view()),
]