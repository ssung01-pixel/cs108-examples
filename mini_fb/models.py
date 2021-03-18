from django.db import models

# Create your models here.

class Profile(models.Model):
    ''' models the data attributes of Facebook users.'''

    # data attributes:
    first_name = models.TextField(blank=True) # creating a first name text field
    last_name = models.TextField(blank=True) # creating a last name text field
    city = models.TextField(blank=True) # creating a city text feild
    email_address = models.TextField(blank=True) # creating a email address text field
    profile_img_url = models.URLField(blank=True) # creating a URL feild for the picture attribute

    def __str__(self):
        '''Return a string representation of this object. '''

        return f'{self.last_name}, {self.first_name}' # how the string is represented on the django admin. 