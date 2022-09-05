import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    
    name = models.CharField(max_length=32, db_index=True, unique=True)
    parent = models.ForeignKey("Department", default=None, null=True, related_name="childsource",on_delete=models.PROTECT)
    uuid = models.CharField(max_length=128, default=uuid.uuid4)
    created_by = models.ForeignKey(User,related_name="cretated_by",on_delete=models.PROTECT)
    updated_by = models.ForeignKey(User,related_name="updated_by",on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%d%s' % self.id, self.name 