# File: forms.py 
# Author: Sarinna Sung, (ssung101@bu.edu), 03/25/2021
# Description: 

from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    ''' A form to create a new Profile object. '''
    first_name = forms.CharField(label="first name", required=True)
    last_name = forms.CharField(label="last name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="city", required=True)
    email_address = forms.CharField(label="email address", required=True)
    
    class Meta:
        ''' additional data about this form '''
        model = Profile # which model to create 
        fields = ['first_name', 'last_name', 'birth_date','city', 'email_address', 'profile_img_url'] # which fields to create 

class UpdateProfileForm(forms.ModelForm):
    ''' A form to be able to update a Profile'''
    first_name = forms.CharField(label="first name", required=True)
    last_name = forms.CharField(label="last name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="city", required=True)
    email_address = forms.CharField(label="email address", required=True)
    class Meta:
        ''' additional data about this form '''
        model = Profile # which to update 
        fields = ['first_name', 'last_name', 'birth_date','city', 'email_address', 'profile_img_url'] # which fields to update