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
]