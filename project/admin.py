# File: mini_fb/admin.py
# Author: Sarinna Sung, (ssung101@bu.edu), 04/16/2021
# Description: this page is used to register the models with the django admin appication project/admin.py

from django.contrib import admin

# Register your models here.
from .models import *
# register the profile model with the django admin application  mini_fb/admin.py

admin.site.register(DailyLog)
admin.site.register(StatusMessage)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Profile) # register our model so we can use it in the built in django model tool

