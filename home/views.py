from django.shortcuts import render

def home_page(request):
    # Your view logic here
    return render(request, 'home_page.html')
