
from django.conf.urls import url

from django.contrib.auth import views as auth_views
from .import views

urlpatterns=[
        url(r'^signup/$',views.signup,name='signup'),
        url(r'^login/$',views.login,name='login')
]
