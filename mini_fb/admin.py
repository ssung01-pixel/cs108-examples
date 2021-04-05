# File: mini_fb/admin.py
# Author: Sarinna Sung, (ssung101@bu.edu), 03/24/2021
# Description: this page is used to register the models with the django admin appication mini_fb/admin.py

from django.contrib import admin

# Register your models here.
from .models import *
# register the profile model with the django admin application  mini_fb/admin.py

admin.site.register(Profile) # register our model so we can use it in the built in django model tool
admin.site.register(StatusMessage) # registering our model so we can use the status message tool
