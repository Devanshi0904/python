from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("cart",cart,name="cart"),
    path("chackout",chackout,name="chackout"),
    path("contact",contact,name="contact"),
    path("shop",shop,name="shop"),
    path("user_registration",user_registration,name='user_registration'),
    path("user_login",user_login,name="user_login"),
    path("user_logout",user_logout,name="user_logout"),
    path("login_register",login_register,name="login_register")
    ]