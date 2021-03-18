from django.db import models

# Create your models here.

class Profile(models.Model):
    ''' models the data attributes of Facebook users.'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email_address = models.TextField(blank=True)
    profile_img_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this object. '''

        return f'{self.last_name}, {self.first_name}'