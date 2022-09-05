
import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
 
class Service(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField(null=True)
 
    def __str__(self):
        return self.name



class Customerinfo(models.Model):
    name = models.CharField(max_length = 200 ,null=False)
    phone= models.IntegerField(null=False)
    email = models.EmailField()
    address= models.CharField(max_length=200)
   
 
    def __str__(self):
        return self.name        

class Emp(models.Model):
    
    name = models.CharField(max_length = 200 ,null=False)
    phone= models.IntegerField(null=False)
    email = models.EmailField()
    address= models.CharField(max_length=200)  
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
      


    def __str__(self) -> str:
        return self.name 