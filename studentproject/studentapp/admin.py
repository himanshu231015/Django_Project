from django.contrib import admin
from django.db import models

# Register your models here.
from studentapp.models import Registration
class RegAdmin(admin.ModelAdmin):
    list_display=['eid','ename','esalr','eadd','unm','pw']
admin.site.register(Registration,RegAdmin)