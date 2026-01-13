from django.contrib import admin
from .models import Todo

# Register your models here.
#Registering the model allows you to manage to-do items via Django’s built-in admin interface.
admin.site.register(Todo)

