from django.contrib import admin

from .models import  Song, Website_Information

#admin.site.register(User,admin)
admin.site.register(Song)
admin.site.register(Website_Information)
# Register your models here.
