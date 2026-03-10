from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# just function take a request and return response
def index(request):
    return HttpResponse("This Works!")
