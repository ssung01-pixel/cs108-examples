# File: models.py
# Author: Sarinna Sung, (ssung101@bu.edu), 04/15/2021
# Description: models.py will model the data attributes of Covid tracking users. Create your models here

from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    ''' models the data attributes of Facebook users.'''
    # data attributes:
    first_name = models.TextField(blank=True) # creating a first name text field
    last_name = models.TextField(blank=True) # creating a last name text field
    date_of_birth =models.DateField(auto_now=True, null=True, blank=True)
    blood_type = models.TextField(blank= True) # creating a blood type
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
        return self.friends.all() # returning all the friends
    
    def get_news_feed(self):
        ''' method on the Profile class that will obtain and return the new feed items. Specifically, this will return a QuerySet of all StatusMessages by this Profile and all of its friends.'''

        news = StatusMessage.objects.all().order_by("-timestamp")  # this is to order all the status message -timestamp is from the newest status message to the oldest.
        # go through lsit and find everybody that profile = that

        friends = self.get_friends() # getting list of all friends

        friends_news = news.filter(profile__in=friends) # filtering people that are only the person in profile's messages

        self_news = news.filter(profile=self.pk)  # filtering people that are only the person in profile's friends 

        total = self_news | friends_news # merging both of the filtered out messeges of the profile's person and their friends

        return total # return the merged messages of profile's person and their friends

    def get_friend_suggestions(self):
        '''  method on the Profile class that will obtain and return a QuerySet of all Profile that could be added as friends. '''
        possible_friends = Profile.objects.exclude(pk__in=self.friends.all()) # getting all the possible friends that are not your friends
        possible_friends = possible_friends.exclude(pk=self.pk) # excluding yourself as a friend
        return possible_friends # returning possible friends

class Doctor(models.Model):
    ''' models the data attributes of Facebook users.'''

    # data attributes:
    first_name = models.TextField(blank=True) # creating a first name text field
    last_name = models.TextField(blank=True) # creating a last name text field
    address = models.TextField(blank= True) # creating a blood type
    city = models.TextField(blank=True) # creating a city text feild
    email_address = models.TextField(blank=True) # creating a email address text field
    profile_img_url = models.URLField(blank=True) # creating a URL feild for the picture attribute

    def __str__(self):
        '''Return a string representation of this object. '''

        return f'{self.last_name}, {self.first_name}' # how the string is represented on the django admin. 
    
    def get_absolute_url(self):
        '''Provide a url to show this object '''

        return reverse('show_doctors_profile_page', kwargs={'pk':self.pk}) #return a URL to show this one profile
    
    def get_news_feed(self):
        ''' method on the Profile class that will obtain and return the new feed items. Specifically, this will return a QuerySet of all StatusMessages by this Profile and all of its friends.'''
        all_appts = Appointment.objects.filter(doctor=self.pk) # get all the appointments with patients

        qs = StatusMessage.objects.none() # empty queryset accumulator variable
        #qs = Appointment.objects.none() # empty queryset accumulator variable

        for appt in all_appts: # pick all the appts each appt
            qs = qs | appt.profile.get_status_messages() # all the appt with the profiles.

        news =qs.order_by("-timestamp")  # this is to order all the status message -timestamp is from the newest status message to the oldest.
        # go through lsit and find everybody that profile = that

        return news # return the merged messages of profile's person and their friends


class StatusMessage(models.Model):
    ''' models the data attributes of Facebook status message. '''

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) # the foreign key to indicate the relationship to the Profile of the creator of this message
    timestamp = models.TimeField(auto_now=True) # creating the time at which this status message was created/saved DateTimeFeild for the date and the time autoadd now is when the message auto generate time was posted at
    message = models.TextField(blank=True) # creating the text of the status message
    image_file = models.ImageField(blank = True) # an actual image
    Oxygen_level = models.TextField(blank= True) # creating a blood type
    emotions = models.TextField(blank=True) # creating a city text feild
    Comments = models.TextField(blank=True) # creating a email address text field


    def __str__(self):
        ''' Return a string representation of this profile. '''
        
        return f'{self.timestamp} {self.message} {self.profile}' # how the string is represented in the django admin

class Appointment(models.Model):
    ''' models the data attributes of Facebook users.'''

    # data attributes:
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False)
    date = models.DateField(auto_now=False, null=True, blank=True) 

    def __str__(self):
        '''Return a string representation of this object. '''

        return f'{self.profile}, {self.doctor}' # how the string is represented on the django admin. 
