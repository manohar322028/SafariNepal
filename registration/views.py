
from django.shortcuts import render,redirect
from .forms import profileform, UsercreateForm, userupdateform
from django.contrib import messages
from django.contrib.auth import login
from django.views.generic import CreateView
# Create your views here.
def profilepage(request):
    if request.method=="POST":
        user_form= userupdateform(request.POST,instance=request.user)
        profile_form=profileform(request.POST,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save() 
            messages.success(request,'Account created successfully!!')
            return render(request,'home.html')
    else:
        user_form=userupdateform(instance=request.user)
        profile_form=profileform(instance=request.user.profile)
    return render(request,'regis.html', {'form':user_form,'p_form':profile_form}) 

def registerpage(request):
    if request.method=="POST":
        user_form=UsercreateForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('destination')
    else:
        user_form=UsercreateForm()       
    return render(request,'registeruser.html',{'form':user_form})        
