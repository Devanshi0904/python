from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("abc",abc,name="abc"),
    path("bestseller",bestseller,name="bestseller"),
    path("cart",cart,name="cart"),
    path("cheackout",cheackout,name="cheackout"),
    path("contact",contact,name="contact"),
    path("shop",shop,name="shop"),
    path("single",single,name="single"),
]