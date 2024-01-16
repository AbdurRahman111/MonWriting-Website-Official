from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helper import generate_slug
from datetime import datetime



class BlogModel(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog_pics')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)

class contact_table(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Table'
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name


class Newsletter_table(models.Model):
    class Meta:
        verbose_name_plural = 'Newsletter Table'
    email = models.CharField(max_length=255)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.email