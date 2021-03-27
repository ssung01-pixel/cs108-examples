# File: view.py
# Author: Sarinna Sung, (ssung101@bu.edu), 03/24/2021
# Description: Create your views here. create a class definition and inherit from
# the ListView. List View allows us to present many objects of one model in a single screen. 

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile                          # import the model that we want to use.
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllProfilesView(ListView): 
    ''' Show the listing on Profile ''' 
    # creating three data attributes
    model = Profile                                  # retrieve Profile objects from the data database
    template_name = "mini_fb/show_all_profiles.html" # create template that I am going to display this data.
    context_object_name = "profiles"                 # name of the variable to access from within the data.

class ShowProfilePageView(DetailView):
    '''Display a single Profile object'''
    model = Profile                                     # retrieve Profile objects from the data database
    template_name = "mini_fb/show_profile_page.html"    # create template that I am going to display this data.
    context_object_name = "profile"                     # name of the variable to access from within the data.
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context
class CreateProfileView(CreateView):
    ''' Create a new Profile Object and store it into the database'''
    model = Profile                                     # retrieve Profile objects from the data database         
    form_class = CreateProfileForm                      # creating the profile form class
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    ''' Update a Profile Object and store it into the database'''
    model = Profile                                     # retrieve Profile objects from the data database         
    form_class = UpdateProfileForm                      # creating the profile form class
    template_name = "mini_fb/update_profile_form.html"  # create template that I am going to display this data.

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)