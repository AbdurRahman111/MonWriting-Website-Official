from django.contrib import admin

from .models import Profile



class show_Profile(admin.ModelAdmin):
    list_display = ['user', 'designation', 'level']
admin.site.register(Profile, show_Profile)