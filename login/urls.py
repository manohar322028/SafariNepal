from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('password_reset/',)
]
