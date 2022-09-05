
from django.db import models
from django.contrib.auth.models import User

class Emp(models.Model):
    
    name = models.CharField(max_length = 200 ,null=False)
    phone= models.IntegerField(null=False)
    email = models.EmailField()
    address= models.CharField(max_length=200)  
    


    def __str__(self) -> str:
        return self.name 


       