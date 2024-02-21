from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about_page(request):
    return HttpResponse("Hello, Blogggg!")