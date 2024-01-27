from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255, default='', null=True, blank=True)
    level_status = (
        ("Level One", "Level One"),
        ("Level Two", "Level Two"),
        ("Pro", "Pro"),
    )
    level = models.CharField(max_length=20, choices=level_status, default="Level One")
    # level = models.CharField(max_length=255, default='', null=True, blank=True)
    image = models.ImageField(default='default_porfile.jpg',upload_to='pofile_pics')
    followers = models.ManyToManyField(User, related_name='followers', default=None, blank=True)
    bio = models.TextField(max_length=200, null=True,blank=True)
    facebook_profile = models.URLField(null=True,blank=True, default='')
    linkedin_profile = models.URLField(null=True,blank=True, default='')
    Instagram_profile = models.URLField(null=True,blank=True, default='')
    twitter_profile = models.URLField(null=True,blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}'


