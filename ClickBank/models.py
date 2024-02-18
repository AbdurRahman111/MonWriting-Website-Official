from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User
import readtime
from django.urls import reverse
# Create your models here.


class ClickBank_Products_Landing_pages_table(models.Model):
    class Meta:
        verbose_name_plural = 'ClickBank Products Landing pages table'
    Title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='Article_images/', blank=True, null=True)
    HopLink = models.URLField(max_length=255, default=None)
    Landing_Page = RichTextField(blank=True, null=True)
    Short_Note = models.TextField(default="", blank=True, null=True)
    tags = models.CharField(max_length=255, default="", blank=True, null=True)
    Read_Time = models.CharField(max_length=255, default="", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_to = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):

        # result = readtime.of_text(self.Description)
        result = readtime.of_html(self.Description)
        self.Read_Time = result.text


        # make random order ID
        my_slug = slugify(self.Title)
        uniqe_confirm = ClickBank_Products_Landing_pages_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.Title))+ "-" + str(count_num)
            if not ClickBank_Products_Landing_pages_table.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(ClickBank_Products_Landing_pages_table, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_landing_page', args=[str(self.slug)])
