from django.contrib import admin

# Register your models here.
from .models import Names,Question

admin.site.register(Names)
admin.site.register(Question)