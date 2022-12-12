from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Homepage response view
def home_page_view(request):
    return HttpResponse("Hello again!")
