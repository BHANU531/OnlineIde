from django.db import models
import sys
# Create your models here.
from django.db import models

# Create your models here.
class user(models.Model):
    full_name = models.CharField(max_length=200)

class submissions(models.Model):
    Acceptance_status ={
        ("S","Sucess"),
        ('E','error'),
        ('p',"pending")
    }
    language = models.CharField(max_length=20)
    code = models.CharField(max_length=3000)
    submission_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1,choices=Acceptance_status)
    user_input = models.CharField(max_length=200,null=True,blank=True)
    user_output = models.CharField(max_length=200,null=True,blank=True)
    user = models.ForeignKey(user,on_delete=models.CASCADE)



