
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    """
    Signup form to allow the user to create the login

    """
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    Phone_Number=forms.CharField(max_length=30, required=False, help_text='Optional')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','Phone_Number', 'password1' , 'password2')


class LoginForm(AuthenticationForm):

     """
     Authenticates the users
     """

     class Meta:
         model=User
         fields = ('username','password') 
