from django.db import models
from Admin.models import *
import Guest.models
#Create your models here.

class Req(models.Model):
     request_details=models.CharField(max_length=50)
     request_date=models.CharField(max_length=50)
     request_status=models.IntegerField(default=0)
     agency=models.ForeignKey("Guest.Agency",on_delete=models.CASCADE)
     casetype=models.ForeignKey(Casetype,on_delete=models.CASCADE)
     user=models.ForeignKey("Guest.User",on_delete=models.CASCADE)
     report=models.FileField(upload_to='AgencyDocs/',default=0)
     amount=models.CharField(max_length=50,default=0)
     payment_status=models.IntegerField(default=0)
     
class Feedback(models.Model):
    feedback_details=models.CharField(max_length=100)
    user=models.ForeignKey("Guest.User",on_delete=models.CASCADE)

class Complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_details=models.CharField(max_length=100)
    user=models.ForeignKey("Guest.User",on_delete=models.CASCADE)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=100)

class Chat(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey("Guest.User", on_delete=models.SET_NULL, default=False, null=True, related_name="from_user")
    to_user = models.ForeignKey("Guest.User", on_delete=models.SET_NULL, default=False, null=True, related_name="to_user")
    from_agency = models.ForeignKey("Guest.Agency", on_delete=models.SET_NULL, default=False, null=True, related_name="from_agency")
    to_agency = models.ForeignKey("Guest.Agency", on_delete=models.SET_NULL, default=False, null=True, related_name="to_agency")
    content = models.BinaryField(max_length=10000)
    
