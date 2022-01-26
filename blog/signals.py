from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Blog,Blogimages
@receiver(post_save,sender=Blog)
def create_blogimages(sender,instance,**kwargs):
    Blogimages.objects.create(bg=instance)
