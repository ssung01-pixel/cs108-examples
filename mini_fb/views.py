# File: view.py
# Author: Sarinna Sung, (ssung101@bu.edu), 03/24/2021
# Description: Create your views here. create a class definition and inherit from
# the ListView. List View allows us to present many objects of one model in a single screen. 

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile                          # import the model that we want to use.
from .forms import CreateProfileForm, UpdateProfileForm

class ShowAllProfilesView(ListView): 
    ''' Show the listing on Profile ''' 
    # creating three data attributes
    model = Profile                                  # retrieve Profile objects from the data database
    template_name = "mini_fb/show_all_profiles.html" # create template that I am going to display this data.
    context_object_name = "profiles"                 # name of the variable to access from within the data.

class ShowProfilePageView(DetailView):
    '''Display a single Profile object'''
    model = Profile                                  # retrieve Profile objects from the data database
    template_name = "mini_fb/show_profile_page.html" # create template that I am going to display this data.
    context_object_name = "profile"                  # name of the variable to access from within the data.

class CreateProfileView(CreateView):
    ''' Create a new Profile Object and store it into the database'''
    model = Profile                                  # which model to create         
    form_class = CreateProfileForm           
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    ''' Update a Profile Object and store it into the database'''
    model = Profile                                  # which model to create         
    form_class = UpdateProfileForm           
    template_name = "mini_fb/update_profile_form.html"
