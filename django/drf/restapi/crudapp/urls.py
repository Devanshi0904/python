from django.urls import path
from crudapp.views import *

urlpatterns = [
    path("view",view_student,name='view'),
    path("add",add_student,name='add'),
    path("viewbyid/<id>",viewbyid,name='viewbyid'),
    path("update/<id>",update_student,name='update')
]