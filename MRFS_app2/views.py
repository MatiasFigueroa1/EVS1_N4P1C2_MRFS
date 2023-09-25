from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista3(request):
    html="""
    <h1 style="color:green">BIENVENIDO</h1>
    <h1> ESTÁS EN LA VISTA 3 </h1>
    <a href="http://127.0.0.1:8000/" >Ir a vista 1</a>
    <a href="http://127.0.0.1:8000/vista2/" >Ir a vista 2</a>
    <a href="/vista4/" >Ir a vista 4</a>
"""

    return HttpResponse(html)

def vista4(request):
    html="""
    <h1 style="color:red">BIENVENIDO</h1>
    <h1> ESTÁS EN LA VISTA 4 </h1>
    <a href="http://127.0.0.1:8000/" >Ir a vista 1</a>
    <a href="http://127.0.0.1:8000/vista2/" >Ir a vista 2</a>
    <a href="/vista3/" >Ir a vista 3</a>
"""

    return HttpResponse(html)
