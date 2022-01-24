from django.db import models
from registration.models import Extendeduser
class UserProfile(models.Model):
    p_photo=models.ImageField()
    education_institute=models.CharField(max_length=100,blank=True)
    system_user=models.OneToOneField(Extendeduser)   