# File: project/urls.py
# Author: Sarinna Sung, ssung101@bu.edu, 04/15/2021
# Description: direct URL requests to view functions project/urls.py 
#              The urls.py file inside the project, which will create a URL mapping from the default URL ('') 
#              to the ShowAllProfilesView. 

from django.urls import path # import the path function from the django urls library
from .views import * # ShowAllProfilesView, ShowProfilePageView our view class definition

#  creating a list of URL patterns to show profile
urlpatterns = [

    path('', ShowAllProfilesView.as_view(), name = "show_all_profiles"),                    #  showing all patients profiles
    path('doctors', ShowAllDoctorsProfilesView.as_view(), name = "doctors"), # showing all the doctors profile
    path('drprofile/<int:pk>',ShowDoctorsProfilePageView.as_view(), name = "show_doctors_profile_page"), # show a specific doctors profile
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name = "show_profile_page"),    #  adding a patients profile
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name = "update_profile"),  # adding an update patients profile
    path('drprofile/<int:pk>/update', UpdateDoctorsProfileView.as_view(), name = "update_doctors_profile"), # updating a doctors profile
    path('profile/<int:pk>/delete', DeleteProfileView.as_view(), name = "delete_profile"), #delete a patients profile
    path('drprofile/<int:pk>/delete', DeleteDoctorsProfileView.as_view(), name = "delete_doctors_profile"), # deleting a doctors profile
    path('create_profile', CreateProfileView.as_view(), name = "create_profile"),           #  adding a create patients profile 
    path('create_doctor_profile', CreateDoctorProfileView.as_view(), name = "create_doctor_profile"), # creating a doctors profile
    path('profile/<int:pk>/post_status', post_status_message, name = "post_status_message"), #  adding a post status message for a patient
    path('profile/<int:profile_pk>/delete_status/<int:status_pk>',DeleteStatusMessageView.as_view(), name = "delete_status_message"), # adding a delete status for the status message for a patient
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name = "news_feed"), # adding a newsfeed page for the patient
    path('drprofile/<int:pk>/doctor_news_feed', ShowDoctorsNewsFeedView.as_view(), name = "doctor_news_feed"), # adding a newsfeed page for the doctor
    path('profile/<int:pk>/show_possible_friends', ShowPossibleFriendsView.as_view(), name = "show_possible_friends"), # showing possible friends for the patient
    path('profile/<int:profile_pk>/add_friend/<int:friend_pk>', add_friend, name = "add_friend"), # adding friend for the patient

]