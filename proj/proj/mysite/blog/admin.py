from django.contrib import admin

# Register your models here.
from .models import restaurant,Post,picture

admin.site.register(restaurant)
admin.site.register(Post)
admin.site.register(picture)