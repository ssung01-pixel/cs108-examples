# File: profile/urls.py
# Author: Sarinna Sung, (ssung101@bu.edu), 03/24/2021
# Description: The urls.py file inside the mini_fb project, which will create a URL mapping from the default URL ('') 
# to the ShowAllProfilesView. 

from django.urls import path # import the path function from the django urls library
from .views import * # ShowAllProfilesView, ShowProfilePageView our view class definition

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name = "show_all_profiles"), #  creating a list of URL patterns 
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name = "show_profile_page"), #  creating a list of URL pattern to show profile
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name = "update_profile"), #  creating a list of URL pattern to show profile
    path('create_profile', CreateProfileView.as_view(), name = "create_profile"), #  creating a list of URL pattern to show profile

]