from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def starting_page(request):
    return HttpResponse("Welcome")

def posts(request):
    pass

def post_details(request):
    pass