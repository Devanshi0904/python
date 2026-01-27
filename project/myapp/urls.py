from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name='index'),
    path("about",about,name='about'),
    path("blog",blog,name='blog'),
    path("contact",contact,name='contact'),
    path("service",service,name='service'),
    path("team",team,name='team'),
    path("logibn",login,name="login"),
    path("register",register,name="register"),
    path("profile",profile,name='profile'),
    path("account_setting",account_setting,name='account_setting')
    
]