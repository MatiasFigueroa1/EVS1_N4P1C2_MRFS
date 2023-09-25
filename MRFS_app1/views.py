from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    html="""


"""

    return HttpResponse(html)

def vista2(request):
    html="""
<h1>AAAA</h1>

"""

    return HttpResponse(html)