from django.urls import path
from myapp.views import *

urlpatterns = [
path("",index,name="index"),
path("cart",cart,name="cart"),
path("chackout",chackout,name="chackout"),
path("contact",contact,name="contact"),
path("shop",shop,name="shop"),
path("login-register",login_register,name="login-register"),
]