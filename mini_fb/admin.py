# mini_fb/admin.py

from django.contrib import admin

# Register your models here.
from .models import *
# register the profile model with the django admin application  mini_fb/admin.py

admin.site.register(Profile) # register our model so we can use it in the built in django model tool
admin.site.register(StatusMessage) 