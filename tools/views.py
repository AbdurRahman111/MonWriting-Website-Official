from django.shortcuts import render

# Create your views here.


def tools_func(request):
    return render(request, 'tools/tools_page.html')

def Dynamic_Alphabet_Color(request):
    return render(request, 'tools/Dynamic_Alphabet_Color.html')

def Motivated_Quotes_Generator(request):
    return render(request, 'tools/Motivated_Quotes_Generator.html')

def Love_Calculator(request):
    return render(request, 'tools/Love_Calculator.html')

def Distance_Converter(request):
    return render(request, 'tools/Distance_Converter.html')

def Time_Coding(request):
    return render(request, 'tools/Time_Coding.html')

def Create_your_Own_Name_QR_code_for_Free(request):
    return render(request, 'tools/Create_your_Own_Name_QR_code_for_Free.html')