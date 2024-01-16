from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.models import User
from account.models import Profile
# Create your models here.
import readtime



class article_chapter(models.Model):
    class Meta:
        verbose_name_plural = 'Article Chapter'
    slug = models.SlugField(default="Auto-Generate", editable=False)
    name = models.CharField(max_length=255)
    Author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        # make random order ID
        my_slug = slugify(self.name)
        uniqe_confirm = article_chapter.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.name))+ "-" + str(count_num)
            if not article_chapter.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(article_chapter, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def total_article_in_chapter(self):
        return Article_table.objects.filter(Chapter=self).count()

    def all_subchapter_under_chapter(self):
        return article_subchapter.objects.filter(Chapter = self)


class article_subchapter(models.Model):
    class Meta:
        verbose_name_plural = 'Article SubChapter'
    slug = models.SlugField(default="Auto-Generate", editable=False)
    name = models.CharField(max_length=255)
    Chapter = models.ForeignKey(article_chapter, on_delete=models.CASCADE)
    Author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        # make random order ID
        my_slug = slugify(self.name)
        uniqe_confirm = article_subchapter.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.name))+ "-" + str(count_num)
            if not article_subchapter.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(article_subchapter, self).save(*args, **kwargs)

    def __str__(self):
        return self.name




class article_category(models.Model):
    class Meta:
        verbose_name_plural = 'Article Category'

    slug = models.SlugField(default="Auto-Generate", editable=False)
    name = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        # make random order ID
        my_slug = slugify(self.name)
        uniqe_confirm = article_category.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.name))+ "-" + str(count_num)
            if not article_category.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(article_category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def total_article(self):
        return Article_table.objects.filter(Category=self).count()


class Article_table(models.Model):
    class Meta:
        verbose_name_plural = 'Article Table'
    Title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    Category = models.ForeignKey(article_category, on_delete=models.CASCADE, blank=True, null=True)
    Chapter = models.ForeignKey(article_chapter, on_delete=models.CASCADE, blank=True, null=True)
    Subchapter = models.ForeignKey(article_subchapter, on_delete=models.CASCADE, blank=True, null=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='Article_images/', blank=True, null=True)
    Short_Description = models.TextField(default="", blank=True, null=True)
    Description = RichTextField(blank=True, null=True)
    tags = models.CharField(max_length=255, default="", blank=True, null=True)
    Read_Time = models.CharField(max_length=255, default="", blank=True, null=True)
    total_views = models.IntegerField(default=0, null=True, blank=True)
    last_hour_views = models.IntegerField(default=0, null=True, blank=True)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.slug

    def get_profile(self):
        if Profile.objects.filter(user=self.Author):
            var_get_profile = Profile.objects.get(user=self.Author)
        else:
            var_get_profile = None
        return var_get_profile

    def save(self, *args, **kwargs):

        # result = readtime.of_text(self.Description)
        result = readtime.of_html(self.Description)
        self.Read_Time = result.text


        # make random order ID
        my_slug = slugify(self.Title)
        uniqe_confirm = Article_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.Title))+ "-" + str(count_num)
            if not Article_table.objects.filter(slug=my_slug):
                break
        if self.slug == "Auto-Generate":
            self.slug = my_slug
        else:
            pass
        super(Article_table, self).save(*args, **kwargs)


class track_views(models.Model):
    class Meta:
        verbose_name_plural = 'Track Views'

    _id = models.AutoField(primary_key=True, editable=False)
    user_uid = models.CharField(max_length=300, null=True, blank=True)

    Article = models.ForeignKey(Article_table, on_delete=models.CASCADE)

    user_ip = models.CharField(max_length=200, null=True, blank=True)
    views = models.IntegerField(null=True, blank=True, default=1)

    device_os = models.CharField(max_length=200, null=True, blank=True)
    device_browser = models.CharField(max_length=200, null=True, blank=True)
    device_type = models.CharField(max_length=200, null=True, blank=True)
    device_model = models.CharField(max_length=200, null=True, blank=True)

    site_url = models.CharField(max_length=200, null=True, blank=True)
    referrer_url = models.CharField(max_length=200, null=True, blank=True)  # should be larger string - dynamic needed

    user_agent = models.CharField(max_length=1000, null=True, blank=True)  # should be larger string - dynamic needed
    timestamp = models.CharField(max_length=200, null=True, blank=True)
    timezone = models.CharField(max_length=200, null=True, blank=True)

    location_longitude = models.CharField(max_length=200, null=True, blank=True)
    location_latitude = models.CharField(max_length=200, null=True, blank=True)
    location_country = models.CharField(max_length=200, null=True, blank=True)
    location_region = models.CharField(max_length=200, null=True, blank=True)
    location_city = models.CharField(max_length=200, null=True, blank=True)
    location_zip = models.CharField(max_length=200, null=True, blank=True)



class search_log(models.Model):
    class Meta:
        verbose_name_plural = 'Search Logs'
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    user_uid = models.CharField(max_length=255, null=True, blank=True)
    search_word = models.CharField(max_length=255, null=True, blank=True)
    Time = models.DateTimeField(default=datetime.now(), blank=True)