from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
from django.contrib.auth.models import User

class Song(models.Model):
    Name = models.CharField(max_length= 100)
    Artists = models.CharField(max_length = 200)
    Album_Name = models.CharField(max_length = 200)
    User_ID = models.ForeignKey(User, on_delete = models.CASCADE)
    Created_Date =  models.DateTimeField('auto_now_add=True')
    Link = models.CharField(max_length = 100)

    def __str__(self):
        return self.Name
       

class Website_Information(models.Model):
    Name = models.CharField(max_length=100)
    Link = models.ForeignKey(Song, on_delete = models.CASCADE)
    Allowed_Flag = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
