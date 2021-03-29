# quotes/urls.py

from django.urls import path
from .views import * #HomePageView, QuotePageView, RandomQuotePageView, PersonPageVie# our view class definition

urlpatterns = [
    path('', RandomQuotePageView.as_view(), name = "random"),
    path('all', HomePageView.as_view(), name = "all_quotes"),
    path('quote/<int:pk>', QuotePageView.as_view(), name = "quote"), # quote/ and then a number django retrieve the quote object that responds to that primary key 
    path('quote/<int:pk>/update', UpdateQuoteView.as_view(), name = "update_quote"), # quote/ and then a number django retrieve the quote object that responds to that primary key 
    path('quote/<int:pk>/delete', DeleteQuoteView.as_view(), name = "delete_quote"), #delete
    path('person/<int:pk>', PersonPageView.as_view(), name = "person"),
    path('person/<int:pk>/add_image', add_image, name = 'add_image'), # add an image for this person
    path('create_quote', CreateQuoteView.as_view(), name = 'create_quote'),
]