from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name="index"),
    path('delete',delete_fruit,name="delete"),
    path('edit',edit_fruit,name="edit")
]