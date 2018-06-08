from django.contrib import admin

# Register your models here.
from .models import Restaurant,Picture
admin.site.register(Restaurant)
admin.site.register(Picture)

