from django.contrib import admin
from myapp.models import *

# Register your models here.
class contryAdmin (admin.ModelAdmin):
    list_display = ['name']
class stateAdmin (admin.ModelAdmin):
    list_display = ['name']
class cityAdmin (admin.ModelAdmin):
    list_display = ['name']


admin.site.register(product)
admin.site.register(contry,contryAdmin)
admin.site.register(state,stateAdmin)
admin.site.register(city,cityAdmin)

