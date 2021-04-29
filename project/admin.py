# File: project/admin.py
# Author: Sarinna Sung, (ssung101@bu.edu), 04/26/2021
# Description: this page is used to register the models with the django admin appication project/admin.py

from django.contrib import admin

# Register your models here.
from .models import *
# register the profile model with the django admin application  project/admin.py

admin.site.register(StatusMessage)# register the statusmessage model to use in django tool
admin.site.register(Doctor)# register the doctor model to use in django tool
admin.site.register(Appointment)# register the appt model to use in django tool
admin.site.register(Profile)# register our model so we can use it in the built in django model tool

