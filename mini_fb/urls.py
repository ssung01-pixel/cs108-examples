# File: profile/urls.py
# Author: Sarinna Sung, (ssung101@bu.edu), 03/24/2021
# Description: The urls.py file inside the mini_fb project, which will create a URL mapping from the default URL ('') 
# to the ShowAllProfilesView. 

from django.urls import path # import the path function from the django urls library
from .views import * # ShowAllProfilesView, ShowProfilePageView our view class definition

#  creating a list of URL patterns to show profile
urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name = "show_all_profiles"),                    #  showing all profiles
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name = "show_profile_page"),    #  adding a profile
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name = "update_profile"),  # adding an update profile
    path('create_profile', CreateProfileView.as_view(), name = "create_profile"),           #  adding a create profile 
    path('profile/<int:pk>/post_status', post_status_message, name = "post_status_message"), #  adding a post status message
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>',DeleteStatusMessageView.as_view(), name = "delete_status_message"), # adding a delete status for the status message
]