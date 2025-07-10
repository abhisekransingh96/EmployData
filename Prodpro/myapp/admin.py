from django.contrib import admin
from .models import *

# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','salary','id']

admin.site.register(Employee,ModelAdmin)