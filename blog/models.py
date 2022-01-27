from django.db import models
from destination.models import Places
import datetime
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=30)
    description=models.TextField()
    thumbnail=models.ImageField(upload_to="blogimages")
    created_date=models.DateField(auto_now_add=True)
    related_place=models.ForeignKey(Places,on_delete=models.CASCADE)

    def __str__(self):
        return self.related_place.name



class Blogimages(models.Model):
    bg=models.ForeignKey(Blog,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True,upload_to="blogimages")

    def __str__(self):
        return self.bg.related_place.name


 
