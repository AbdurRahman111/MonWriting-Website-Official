from django.db import models
from home.helper import generate_slug
# Create your models here.


class tools_page_list(models.Model):
    class Meta:
        verbose_name_plural = 'Tools Pages'
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='Tools_Image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_to = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(tools_page_list, self).save(*args, **kwargs)