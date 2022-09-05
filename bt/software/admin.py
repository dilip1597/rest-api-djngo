from django.contrib import admin
from .models import SoftwareType,SoftwreSubType,Software,ComputerSoftwareType

# Register your models here.
admin.site.register(SoftwareType)
admin.site.register(SoftwreSubType)
admin.site.register(Software)
admin.site.register(ComputerSoftwareType)