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
    friends = models.ManyToManyField("self", blank=True) # blank = true that means not everything is not required. one profile doesnt need friends self is refereed to the profile object

    def __str__(self):
        '''Return a string representation of this object. '''

        return f'{self.last_name}, {self.first_name}' # how the string is represented on the django admin. 

    def get_status_messages(self): 
        ''' Return a status messages for this Profile.'''
        return StatusMessage.objects.filter(profile=self) # getting the status messages

    def get_absolute_url(self):
        '''Provide a url to show this object '''
        return reverse('show_profile_page', kwargs={'pk':self.pk}) #return a URL to show this one profile

    def get_friends(self):
        ''' on class Profile that will return all friends for this Profile. '''
        return self.friends.all()
    
    def get_news_feed(self):
        ''' method on the Profile class that will obtain and return the new feed items. Specifically, this will return a QuerySet of all StatusMessages by this Profile and all of its friends.'''

        news = StatusMessage.objects.all().order_by("-timestamp")  # this is to order all the status message -timestamp is from the newest status message to the oldest.
        # go through lsit and find everybody that profile = that

        friends = self.get_friends() # getting list of all friends

        friends_news = news.filter(profile__in=friends) # filtering people that are only the person in profile's messages

        self_news = news.filter(profile=self.pk)  # filtering people that are only the person in profile's friends 

        total = self_news | friends_news # merging both of the filtered out messeges of the profile's person and their friends

        return total # return the merged messages of profile's person and their friends

class StatusMessage(models.Model):
    ''' models the data attributes of Facebook status message. '''

    timestamp = models.TimeField(auto_now=True) # creating the time at which this status message was created/saved DateTimeFeild for the date and the time autoadd now is when the message auto generate time was posted at
    message = models.TextField(blank=True) # creating the text of the status message
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) # the foreign key to indicate the relationship to the Profile of the creator of this message
    image_file = models.ImageField(blank = True) # an actual image

    def __str__(self):
        ''' Return a string representation of this profile. '''
        
        return f'{self.timestamp} {self.message} {self.profile}' # how the string is represented in the django admin

