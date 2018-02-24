from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,get_object_or_404
from django.template import RequestContext, Template
# importing models here 
from django.contrib.auth.models import User
from django.db.models import Q
from .models import  MusicInterest
from django.template import loader
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from googleapiclient.discovery import build



from django.views.generic.edit import CreateView
from django.views.generic import  ListView,DetailView




import pprint
#def index(request):
#    template = loader.get_template('signup.html')    
 #   return HttpResponse(template.render(request))

#def signup(request):
 #   if request.method == 'POST':
  #      form = SignUpForm(request.POST)
   #     #user_obj=get_object_or_404(User)
    #    try:
     #       user_exists = User.objects.get(username=request.POST['username'])
      #      return HttpResponse("Username already taken")
       # except User.DoesNotExist:        
        #    if form.is_valid():
         #       form.save()
          #      user=User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
           #     user.first_name = form.cleaned_data['first_name']
            #    user.last_name = form.cleaned_data['last_name']
             #   user.save()
              #  user = authenticate(username=username, password=raw_password)
           # return redirect('login')
    #else:
     #   form = SignUpForm()
    #return render(request, 'signup.html', {'form': form})


class signup(CreateView):
    model = User
    fields = ['first_name','last_name','email','date_joined' ,'username','password']
#return redirect('login')

class login(CreateView):
    model = User
    fields = ['username','password']


class SongsListView(DetailView):
  

    def get_object(self,*args,**kwargs):
      print (self.kwargs)
      song_id= self.kwargs.get('song_id')
      obj = get_object_or_404(MusicInterest,id=self.kwargs.get('song_id'))
      print obj
      return obj

#class UserDetailView(ListView):
      #return User.objects.all()
#return queryset
#def login(request):
 #   if request.method == 'POST':
 #       form = LoginForm(request.POST)
 #       if form.is_valid():
 #           user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
 #          # login(request)
 #           return redirect('info')
 #   else:
 #       form = LoginForm()
 #   return render(request, 'login.html', {'form': form})

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



def results(request):
# Build a service object for interacting with the API. Visit
# the Google APIs Console <http://code.google.com/apis/console>
# to get an API key for your own application.
  service = build("Canticle", "v1",
developerKey="AIzaSyDas2ovYHFwlhA_UpFyPhNvS_kuD2QoJKI")
  res = search.cse().list(
q='Ed Sheeran',
cx='005828409068220044640:aza23wb-b2e',
    ).execute()
  return HttpResponse(res)
