
from django.db import models
import datetime
from django.contrib.auth.models import User

from django.utils import timezone
<<<<<<< HEAD
class rating(models.Model):
    rate=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)]) 
=======



>>>>>>> 88568b2e8158db3f4589c9e947c9dc42697f221d
   

class Places(models.Model):
    name=models.CharField(max_length=30,null=True,blank=True)
    address=models.CharField(max_length=30)
    descrption=models.TextField()
<<<<<<< HEAD
    thumbnail_image=models.ImageField(upload_to="images")



class destimages(models.Model):
    place=models.ForeignKey(places,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images")


class hotel(models.Model):
=======
    thumbnail_image=models.ImageField(upload_to="images",null=True,blank=True)
    ratings=models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
class Place_rating(models.Model):
    rate=models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)],default=0)
    place=models.ForeignKey(Places,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Comment(models.Model):
    place=models.ForeignKey(Places,related_name="review",on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    comment_body= models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s - %s' %(self.place.name,self.name)


class Destimages(models.Model):
    place=models.ForeignKey(Places,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.place.name



class Hotel(models.Model):
>>>>>>> 88568b2e8158db3f4589c9e947c9dc42697f221d
    title=models.CharField(max_length=20)
    contact_info=models.CharField(max_length=15)
    nearby=models.ForeignKey(Places,on_delete=models.CASCADE)

    def __str__(self):
        return self.nearby.name







        





