from django.db import models
from destination.models import places
import datetime
# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    created_date=models.DateField(default=datetime.now())
    related_place=models.ForeignKey(places)


class blogimages(models.Model):
    bg=models.ForeignKey(blog,on_delete=models.CASCADE)
    image=models.ImageField()