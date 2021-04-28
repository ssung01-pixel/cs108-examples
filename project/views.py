# file: project/view.py
# Author: Sarinna Sung, ssung101@bu.edu, 04/15/2021
# description: provide a view to send to the user.

from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
    
class ShowAllProfilesView(ListView): 
    ''' Show the listing on Profile ''' 
    # creating three data attributes
    model = Profile                                  # retrieve Profile objects from the data database
    template_name = "project/show_all_profiles.html" # create template that I am going to display this data.
    context_object_name = "profiles"                 # name of the variable to access from within the data.


class ShowAllDoctorsProfilesView(ListView):
    ''' Show the listing of the Doctors profile'''
    model = Doctor
    template_name = "project/show_all_doctors_profiles.html"
    context_object_name = "drprofiles"

class ShowDoctorsProfilePageView(DetailView):
    '''Display a single Profile object'''
    model = Doctor                                   # retrieve Profile objects from the data database
    template_name = "project/show_doctors_profile_page.html"    # create template that I am going to display this data.
    context_object_name = "profile"                     # name of the variable to access from within the data.
    
class ShowProfilePageView(DetailView):
    '''Display a single Profile object'''
    model = Profile                                     # retrieve Profile objects from the data database
    template_name = "project/show_profile_page.html"    # create template that I am going to display this data.
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
    template_name = "project/create_profile_form.html"

class CreateDoctorProfileView(CreateView):
    ''' Create a new Profile Object and store it into the database'''
    model = Profile                                     # retrieve Profile objects from the data database         
    form_class = CreateDoctorProfileForm                      # creating the profile form class
    template_name = "project/create_doctor_profile_form.html"

class UpdateProfileView(UpdateView):
    ''' Update a Profile Object and store it into the database'''
    model = Profile                                     # retrieve Profile objects from the data database         
    form_class = UpdateProfileForm                      # creating the profile form class
    template_name = "project/update_profile_form.html"  # create template that I am going to display this data.

class UpdateDoctorsProfileView(UpdateView):
    ''' Update a Profile Object and store it into the database'''
    model = Profile                                     # retrieve Profile objects from the data database         
    form_class = UpdateProfileForm                      # creating the profile form class
    template_name = "project/update_doctor_profile_form.html"  # create template that I am going to display this data.

class DeleteProfileView(DeleteView):
    ''' Update a Profile Object and remove it into the database'''                            
    template_name = "project/delete_profile_form.html"  # create template that I am going to display this data.
    queryset = Profile.objects.all()
    #success_url = "../../all"

    def get_success_url(self):
        ''' Return a the URL to which we should be directed after the delete. '''
        
        # get the pk for this quote
        pk = self.kwargs.get('pk') # find the pk of the quote being deleted
        profile = Profile.objects.filter(pk=pk).first() # get one object form QuerySet

        # find the person associated with the quote
        # person = profile.profile1
        return reverse('show_all_profiles') # show the person page for 

        #reverse to show the person page

def post_status_message(request, pk):
    ''' Process a form submission to post a new status message. '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

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

class DeleteStatusMessageView(DeleteView):
    ''' Create a new profile object and store it into the database'''                                          
    template_name = "project/delete_status_form.html"
    queryset = Profile.objects.all()
    success_url = "../../all" # what to do after deleting a quote

    def get_context_data(self, **kwargs):
        ''' Return a dictionary with context data for this template to use. '''

        # get the default context data:
        # this will include theDeleteStatusMessageView record for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])

        # what is inside the brackets is the inside of URL, st_msg as the key and value as well. storing this new object into the dictionary.
        context['st_msg']= st_msg 

        #return the context dictionary:
        return context

    def get_object(self):
        ''' the objective of which is to return the StatusMessage object that should be deleted. '''
        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object
        status = StatusMessage.objects.filter(pk = status_pk , profile=profile_pk) # get one object form QuerySet

        # return status message object
        return status 

    def get_success_url(self):
        ''' Return a the URL to which we should be directed after the delete. '''
        # read the URL data values into variables
        # get the pk for the profile and status 
        profile_pk = self.kwargs['profile_pk'] # find the profile_pk of the message being deleted

        #attribute(models.py) = variable (local to this function)
        profile = Profile.objects.filter(pk=profile_pk).first() # get one object form QuerySet
        
        #find the person associated with the message
        # using profile.pk is the same right now as profile_pk but its better to use profile.pk
        # _ using to name variables in python
        # . is the class and then accessessing the attribute profile.pk
        return reverse('show_profile_page', kwargs ={'pk':profile.pk}) 

class ShowNewsFeedView(DetailView):
    ''' This base class will do everything we want, without overriding any methods.
    Set the template_name and model attributes as you have done in the past when using the DetailView. '''
    model = Profile                                     # retrieve Profile objects from the data database
    template_name = "project/show_news_feed.html"    # create template that I am going to display this data.
    context_object_name = "profile"                     # name of the variable to access from within the data.

class ShowPossibleFriendsView(DetailView):
    '''  which inherits from the generic DetailView class. The base class will do everything we want, without overriding any methods.'''
    model = Profile # retrieve Profile objects from the data database
    template_name = "project/show_possible_friends.html" # create template that I am going to display this data.

def add_friend(request, profile_pk, friend_pk):
    ''' The objective of this function is to process the add_friend request, to add a friend for a given profile. '''
    profile = Profile.objects.get(pk=profile_pk) # getting our profile object
    friend = Profile.objects.get(pk=friend_pk) # getting your friends profile object
    
    profile.friends.add(friend) # adding the profile of the friends and adding that friend to your friend list
    profile.save() # saving that profile 

    url = reverse('show_profile_page', kwargs={'pk': profile_pk}) # going to the show profile page and the profile originally
    return redirect(url) # redirecting you to that url

