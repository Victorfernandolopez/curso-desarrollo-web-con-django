
import requests
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect("https://api.recursospython.com/dollar")