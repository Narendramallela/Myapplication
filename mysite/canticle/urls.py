
from django.conf.urls import url

from django.contrib.auth import views as auth_views
from .import views

urlpatterns=[
        url(r'^signup/$',views.signup,name='signup'),
        url(r'^login/$',views.login,name='login'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^login/info/$',views.info,name='info'),
        url(r'^login/addanentry/$',views.addanentry,name='addanentry'),
        
]
