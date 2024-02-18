from django.urls import path
from . import views


urlpatterns = [
    path('', views.clickbank_products, name="clickbank_products"),
    path('Sugar-Defender', views.Sugar_Defender, name="Sugar_Defender"),
    path('Sugar-Defender-2', views.Sugar_Defender_2, name="Sugar_Defender_2"),
    path('Cortexi-Hearing-Support', views.Cortexi_Hearing_Support, name="Cortexi_Hearing_Support"),
    path('<str:slug>', views.product_landing_page, name="product_landing_page"),
]