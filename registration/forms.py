from django.forms import ModelForm 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, preferences

class UsercreateForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username','email','password1','password2']

class profileform(ModelForm):
    class Meta:
        model= Profile
        fields= ['middle_name','sex','age','phone_number','nationality','profile_pic']

class userupdateform(ModelForm):
    class Meta:
        model= User
        fields= ['username','email','first_name','last_name']

class preferenceform(forms.Form):
    Choice=[('yes','yes'),('no','no')]
    culture=forms.ChoiceField(choices=Choice,widget=forms.RadioSelect)
    adventure=forms.ChoiceField(choices=Choice,widget=forms.RadioSelect)
    wildlife=forms.ChoiceField(choices=Choice,widget=forms.RadioSelect)
    sightseeing=forms.ChoiceField(choices=Choice,widget=forms.RadioSelect)
    sightseeing=forms.ChoiceField(choices=Choice,widget=forms.RadioSelect)
    class Meta:
        model= preferences
