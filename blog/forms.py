from django import forms
from django.forms import ModelForm
from .models import blog,blogimages

class blogcreateform(ModelForm):
    class Meta:
        model= blog
        fields=['title','description']         

