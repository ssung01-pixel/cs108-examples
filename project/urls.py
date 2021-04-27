# file: project/urls.py
# author: Sarinna Sung, ssung101@bu.edu, 04/15/2021
# description: direct URL requests to view functions

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
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name = "news_feed"), # adding a newsfeed page
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name = "show_possible_friends"), # showing possible friends
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name = "add_friend"), # adding friend 
    path('create_doctor_profile', CreateDoctorProfileView.as_view(), name = "create_doctor_profile"),
]