from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# software type master
class SoftwareType(models.Model):
    name = models.CharField(max_length=32, db_index=True, unique=True)
    discription = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User,related_name="type_cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="type_updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __repr__ (self):
        return '<Type %s >' % (self.name)
    
    def __str__ (self):
        return self.name


# Software sub type master 
class SoftwreSubType(models.Model):
    software_type = models.ForeignKey("SoftwareType", default=None, null=True, related_name="SoftwareType",on_delete=models.PROTECT)
    name = models.CharField(max_length=32, db_index=True, unique=True)
    discription = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User,related_name="sub_type_cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="sub_type_updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __repr__ (self):
        return '<Type %s >' % (self.name)

    def __str__ (self):
        return self.name

# Software list mster
class Software(models.Model):
    class Meta:
        unique_together = (('name', 'version'),)

    software_sub_type = models.ForeignKey("SoftwreSubType", default=None, null=True, related_name="SoftwreSubType",on_delete=models.PROTECT)
    computer_software_type = models.ForeignKey("ComputerSoftwareType", default=None, null=True, related_name="ComputerSoftwareType",on_delete=models.PROTECT)
    name = models.CharField(blank=False, null=False, max_length=512)
    version = models.TextField(null=True, blank=True)
    port_numbers = models.TextField(null=True, blank=True)
    # more than one sub type then add it 
    sub_types = models.TextField(null=True, blank=True)
    discription = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User,related_name="software_cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="software_updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __repr__ (self):
        return '<Type %s >' % (self.name)

    def __str__ (self):
        return self.name

# Computer Software type
class ComputerSoftwareType(models.Model):
    name = models.CharField(max_length=32, db_index=True, unique=True)
    discription = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User,related_name="ComputerSoftwareType_cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="ComputerSoftwareType_updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __repr__ (self):
        return '<Type %s >' % (self.name)
    
    def __str__ (self):
        return self.name


# Sotware trasaction 

# server software list 



# ssh login details
    # sudo user 

# mysql loing 
    # grants list 

# postgress login 
    # grants 



