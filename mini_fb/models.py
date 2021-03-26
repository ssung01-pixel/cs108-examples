# File: models.py
# Author: Sarinna Sung, (ssung101@bu.edu), 03/24/2021
# Description: models.py will model the data attributes of Facebook users. Create your models here

from django.db import models
from django.urls import reverse

class Profile(models.Model):
    ''' models the data attributes of Facebook users.'''

    # data attributes:
    first_name = models.TextField(blank=True) # creating a first name text field
    last_name = models.TextField(blank=True) # creating a last name text field
    city = models.TextField(blank=True) # creating a city text feild
    email_address = models.TextField(blank=True) # creating a email address text field
    profile_img_url = models.URLField(blank=True) # creating a URL feild for the picture attribute

    def __str__(self):
        '''Return a string representation of this object. '''

        return f'{self.last_name}, {self.first_name}' # how the string is represented on the django admin. 

    def get_status_messages(self): 
        ''' Return a status messages for this Profile.'''
        return StatusMessage.objects.filter(profile=self) # getting the status messages

    def get_absolute_url(self):
        '''Provide a url to show this object '''
        return reverse('show_profile_page', kwargs={'pk':self.pk})

class StatusMessage(models.Model):
    ''' models the data attributes of Facebook status message. '''

    timestamp = models.TimeField(auto_now = True) # creating the time at which this status message was created/saved
    message = models.TextField(blank=True) # creating the text of the status message
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) # the foreign key to indicate the relationship to the Profile of the creator of this message

    def __str__(self):
        ''' Return a string representation of this profile. '''
        
        return f'{self.timestamp} {self.message} {self.profile}' # how the string is represented in the django admin

