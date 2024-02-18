from django.shortcuts import render
from .models import ClickBank_Products_Landing_pages_table
# Create your views here.


def clickbank_products(request):
    get_all_products_pages = ClickBank_Products_Landing_pages_table.objects.all()
    context = {'get_all_products_pages':get_all_products_pages}
    return render(request, 'clickbank/clickbank_products.html', context)

def product_landing_page(request, slug):
    get_landing_page_by_slug = ClickBank_Products_Landing_pages_table.objects.get(slug=slug)
    context={'get_landing_page_by_slug':get_landing_page_by_slug}
    return render(request, 'clickbank/clickbank_products.html', context)