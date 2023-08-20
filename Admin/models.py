from django.db import models

# Create your models here.

class District(models.Model):
    district_name=models.CharField(max_length=100)

    def __str__(self):
        return self.district_name

class Place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name

class Casetype(models.Model):
    casetype_name=models.CharField(max_length=50)

    def __str__(self):
        return self.casetype_name




