from django.urls import path
from . import views


urlpatterns = [
    path('', views.clickbank_products, name="clickbank_products"),
    path('<str:slug>', views.product_landing_page, name="product_landing_page"),
]