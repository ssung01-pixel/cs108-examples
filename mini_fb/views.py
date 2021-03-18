from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile # import the model that we want to use.
# Create your views here.

# create a class definition and inherit from the ListView. List View allows us to present many objects of one model in a single screen. 

class ShowAllProfilesView(ListView): 
    ''' Show the listing on Profile ''' 

    # creating three data attributes

    model = Profile # retrieve Profile objects from the data database
    template_name = "mini_fb/show_all_profiles.html" # create template that I am going to display this data.
    context_object_name = "profiles" # name of the variable to access from within the data.