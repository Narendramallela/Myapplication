from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.template import RequestContext, Template
# importing models here 

from .models import User, Song, Website_Information
from django.template import loader
from .forms import SignUpForm
from .forms import AuthenticationForm

def index(request):
    template = loader.get_template('signup.html')    
    return HttpResponse(template.render(request))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
        
            login(request, user)
        user_obj = User(username=username, email=email, password=password)
        # saving all the data in the current object into the database
        user_obj.save()
          # saving all the data in the current object into the database
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def info(request):
    recently_added_song_list = Song.objects.order_by('-Name')[:5]
    template = loader.get_template('info.html')
    context = {
        'recently_added_song_list': recently_added_song_list,
    }
    return HttpResponse(template.render(context, request))

def logout(request):
    output="You are successfully logged out of Canticle"
    return HttpResponse(output)
