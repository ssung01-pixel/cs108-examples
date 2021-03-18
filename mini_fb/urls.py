# profile/urls.py

from django.urls import path # import the path function from the django urls library
from .views import ShowAllProfilesView # our view class definition

urlpatterns = [
    path('', ShowAllProfilesView.as_view(), name = "show_all_profiles"), #  creating a list of URL patterns 

]