from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
def xyz(request):
    return HttpResponse("<h1>This is h1 tag</h1>")