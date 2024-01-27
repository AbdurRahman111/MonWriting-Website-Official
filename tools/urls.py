from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.tools_func, name="tools_func"),
    path('Dynamic-Alphabet-Color/', views.Dynamic_Alphabet_Color, name="Dynamic_Alphabet_Color"),
    path('Motivated-Quotes-Generator/', views.Motivated_Quotes_Generator, name="Motivated_Quotes_Generator"),
    path('Love-Calculator/', views.Love_Calculator, name="Love_Calculator"),
    path('Distance-Converter/', views.Distance_Converter, name="Distance_Converter"),
    path('Time-Coding/', views.Time_Coding, name="Time_Coding"),
    path('Create-your-Own-Name-QR-code-for-Free/', views.Create_your_Own_Name_QR_code_for_Free, name="Create_your_Own_Name_QR_code_for_Free"),

    path('YouTube-Thumbnail-Downloader/', views.YouTube_Thumbnail_Downloader, name="YouTube_Thumbnail_Downloader"),
    path('Word-and-Character-Counter-Tool/', views.Word_and_Character_Counter_Tool, name="Word_and_Character_Counter_Tool"),
    path('About-Us-Page-Generator-for-Website/', views.About_Us_Page_Generator_for_Website, name="About_Us_Page_Generator_for_Website"),
    path('Password-generator-zone/', views.Password_generator_zone, name="Password_generator_zone"),
    path('Active-Voice-to-Passive-Voice-Converter/', views.Active_Voice_to_Passive_Voice_Converter, name="Active_Voice_to_Passive_Voice_Converter"),
    path('BMI-Calculator/', views.BMI_Calculator, name="BMI_Calculator"),
    path('Flower-Coding/', views.Flower_Coding, name="Flower_Coding"),
    path('Pregnancy-Calculator/', views.Pregnancy_Calculator, name="Pregnancy_Calculator"),
    path('Currency-Converter-Tool/', views.Currency_Converter_Tool, name="Currency_Converter_Tool"),
    path('PNG-to-JPG-Image/', views.PNG_to_JPG_Image, name="PNG_to_JPG_Image"),
    path('Age-Calculate-Calculator/', views.Age_Calculate_Calculator, name="Age_Calculate_Calculator"),
    path('Area-Calculate-Calculator/', views.Area_Calculate_Calculator, name="Area_Calculate_Calculator"),
    path('Percentage-Calculate-Calculator/', views.Percentage_Calculate_Calculator, name="Percentage_Calculate_Calculator"),
]