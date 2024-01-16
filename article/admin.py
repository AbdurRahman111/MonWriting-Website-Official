from django.contrib import admin
from .models import Article_table, article_category, article_chapter, article_subchapter, track_views, search_log
# Register your models here.


class show_Article_table(admin.ModelAdmin):
    list_display = ['Title', 'Category', 'Author', 'Time']
    readonly_fields = ['total_views', 'last_hour_views', 'Read_Time']
admin.site.register(Article_table, show_Article_table)

class show_search_log(admin.ModelAdmin):
    list_display = ['user', 'user_uid', 'search_word', 'Time']
admin.site.register(search_log, show_search_log)


class show_track_views(admin.ModelAdmin):
    list_display = ['user_uid', 'Article', 'user_ip', 'views', 'device_os', 'device_browser', 'timestamp', 'timezone']
admin.site.register(track_views, show_track_views)

admin.site.register(article_category)
admin.site.register(article_chapter)
admin.site.register(article_subchapter)