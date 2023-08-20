from django.db import models
from Admin.models import *
from User.models import *
from Agency.models import *

# Create your models here.

class User(models.Model):
    user_name=models.CharField(max_length=50)
    user_address=models.CharField(max_length=100)
    user_mail=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='UserDocs/')
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    user_pass=models.CharField(max_length=50)
    user_regdate=models.DateField(auto_now_add=True)
    key=models.BinaryField(max_length=1000,null=True)


class Agency(models.Model):
    agency_name=models.CharField(max_length=50)
    agency_address=models.CharField(max_length=200)
    agency_mail=models.CharField(max_length=100)
    agency_pass=models.CharField(max_length=50)
    agency_proof=models.FileField(upload_to='AgencyDocs/')
    agency_photo=models.FileField(upload_to='AgencyDocs/')
    agency_contact=models.CharField(max_length=50)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    agency_vstatus=models.IntegerField(default=0)
    casetype=models.ForeignKey(Casetype,on_delete=models.CASCADE)
    agency_regdate=models.DateField(auto_now_add=True)
    key=models.BinaryField(max_length=1000,null=True)   

class admin(models.Model):
    admin_mail=models.CharField(max_length=100)
    admin_pass=models.CharField(max_length=50)
