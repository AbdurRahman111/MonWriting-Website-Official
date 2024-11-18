from django.shortcuts import render

# Create your views here.


def my_earnings(request):
    return render(request, "my_earnings.html")