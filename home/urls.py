from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name="index"),
    path('privacy-policy/', views.privacy_policy, name="privacy_policy"),
    path('searchbar', views.searchbar, name="searchbar"),
    path('function_all_categories', views.function_all_categories, name="function_all_categories"),
    path('category-articles/<str:slug>', views.category_articles, name="category_articles"),
    path('article-details/<str:slug>', views.article_details, name="article_details"),
    path('follow-writer', views.follow_writer, name="follow_writer"),
    path('writer/<str:username>', views.writer, name="writer"),
    path('subchapter/<str:slug>', views.subchapter, name="subchapter"),
    path('user-profile', views.user_profile, name="user_profile"),
    path('contact', views.contact, name="contact"),
    path('article-page', views.article_page, name="article_page"),
    path('article-page/details', views.article_page_details, name="article_page_details"),
    path('test', views.test, name="test"),
    path('submit_newsletter', views.submit_newsletter, name="submit_newsletter"),
    path('Blogging', views.Blogging, name="Blogging"),
    path('edit_article/<str:slug>', views.edit_article, name="edit_article"),
    path('getsubchapters', views.getsubchapters, name="getsubchapters"),

    # google adsense
    path('ads.txt', TemplateView.as_view(template_name="ads.txt", content_type='text/plain')),
]