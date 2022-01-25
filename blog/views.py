from django.shortcuts import render

# Create your views here.
def view_blog(request):
    return render(request,'blog.html')
    
def blogpost(request):
    return render(request,'blogpost.html')
        