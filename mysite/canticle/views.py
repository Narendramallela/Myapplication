from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django.template import RequestContext, Template
# importing models here 
from django.contrib.auth.models import User
from .models import  Song, Website_Information
from django.template import loader
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate

def index(request):
    template = loader.get_template('signup.html')    
    return HttpResponse(template.render(request))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #user_obj=get_object_or_404(User)
        try:
            user_exists = User.objects.get(username=request.POST['username'])
            return HttpResponse("Username already taken")
        except User.DoesNotExist:        
            if form.is_valid():
                form.save()
                user=User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password1 = form.cleaned_data['password1'], password2=form.cleaned_data['password2'])
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                user = authenticate(username=username, password=raw_password)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
           # login(request)
            return redirect('info')
    else:
        form = LoginForm()
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


def addanentry(request):
    return redirect('addanentry')
