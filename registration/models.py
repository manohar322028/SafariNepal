from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class preferences(models.Model):
     culture=models.BooleanField(default=False)
     wildlife=models.BooleanField(default=False)
     adventure=models.BooleanField(default=False)
     sightseeing=models.BooleanField(default=False)
     history=models.BooleanField(default=False)


class Profile(models.Model):
    middle_name= models.CharField(max_length=20,null=True,blank=True)
    sex=models.CharField(max_length=10,choices=[('MALE','MALE'),('FEMALE','FEMALE')])
    age=models.IntegerField(null=True,blank=True)
    phone_number=models.CharField(max_length=15,null=True,blank=True)
    nationality=models.CharField(max_length=20,null=True,blank=True)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True,blank=True)
    preference=models.OneToOneField(preferences,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.username
    
