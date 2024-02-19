# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse
from article.models import article_chapter, article_subchapter, article_category, Article_table
from tools.models import tools_page_list
from ClickBank.models import ClickBank_Products_Landing_pages_table

class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        # List the names of the views you want to include
        return ['index', 'privacy_policy', 'contact', 'article_page', 'tools_func', 'Dynamic_Alphabet_Color', 'Motivated_Quotes_Generator', 'Love_Calculator', 'Distance_Converter', 'Time_Coding', 'Create_your_Own_Name_QR_code_for_Free', 'YouTube_Thumbnail_Downloader', 'Word_and_Character_Counter_Tool', 'About_Us_Page_Generator_for_Website', 'Password_generator_zone', 'Active_Voice_to_Passive_Voice_Converter', 'BMI_Calculator', 'Flower_Coding', 'Pregnancy_Calculator', 'Currency_Converter_Tool', 'PNG_to_JPG_Image', 'Age_Calculate_Calculator', 'Area_Calculate_Calculator', 'Percentage_Calculate_Calculator', 'YouTube_Video_Downloader', 'Tic_Tac_Toe_game', 'about_us', 'Sugar_Defender', 'Cortexi_Hearing_Support' ,'Sugar_Defender_prod']  # Add more view names as needed

    def location(self, item):
        # Use the reverse function to get the URL for each view
        return reverse(item)


# class ArticleChapterSitemap(sitemaps.Sitemap):
#     changefreq = 'weekly'
#     priority = 0.9
#
#     def items(self):
#         return article_chapter.objects.all()
#
#     def lastmod(self, obj):
#         return obj.updated_to  # Adjust this based on your model field


class ArticleSubChapterSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return article_subchapter.objects.all()

    def lastmod(self, obj):
        return obj.updated_to  # Adjust this based on your model field

class ArticleCategorySitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return article_category.objects.all()

    def lastmod(self, obj):
        # You may want to set the last modification date based on articles within the category
        # For simplicity, it is set to the current time here.
        # return datetime.now()
        return obj.updated_to

class ArticleTableSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Article_table.objects.all()

    def lastmod(self, obj):
        return obj.updated_to  # Adjust this based on your model field


class ToolsSitemap(sitemaps.Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return tools_page_list.objects.all()

    def lastmod(self, obj):
        # Adjust this based on your model field
        return obj.updated_to


class ClickBank_Products_Landing_pages_table_Sitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return ClickBank_Products_Landing_pages_table.objects.all()

    def lastmod(self, obj):
        return obj.updated_to  # Adjust this based on your model field



# Add more sitemap classes if needed

