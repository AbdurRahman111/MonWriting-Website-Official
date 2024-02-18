from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "MonWriting"
admin.site.site_title = "MonWriting Admin Panel"
admin.site.index_title = "MonWriting Admin Panel"

from django.contrib.sitemaps.views import sitemap
from home.sitemaps import (
    StaticViewSitemap,
    # ArticleChapterSitemap,
    ArticleSubChapterSitemap,
    ArticleCategorySitemap,
    ArticleTableSitemap,
    ToolsSitemap,
)

sitemaps = {
    'Static_urls': StaticViewSitemap,
    # 'article_chapters': ArticleChapterSitemap,
    'article_subchapters': ArticleSubChapterSitemap,
    'article_categories': ArticleCategorySitemap,
    'article_tables': ArticleTableSitemap,
    'tools': ToolsSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('tools/', include('tools.urls')),
    path('CB/', include('ClickBank.urls')),
    path('froala_editor/',include('froala_editor.urls')),

    #sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)