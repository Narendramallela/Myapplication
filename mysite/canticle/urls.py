
from django.conf.urls import url

from django.contrib.auth import views as auth_views
from canticle.views import  signup, login, SongsListView, UserDetailView



from .import views

urlpatterns=[
        url(r'^$',signup.as_view()),
        url(r'^login/$',login.as_view()),
        url(r'^list/(?P<song_id>\d+)/$',SongsListView.as_view()),
        url(r'^userprofile/(?P<user_id>\d+)/$',UserDetailView.as_view()),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^login/info/$',views.info,name='info'),
        url(r'^login/addanentry/$',views.addanentry,name='addanentry'),
        url(r'^login/results/$',views.results, name='results'),
        
]
