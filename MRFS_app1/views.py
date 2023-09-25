from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    html="""
    <h1 style="color:blue">BIENVENIDO</h1>
    <h1> ESTÁS EN LA VISTA 1 </h1>
    <a href="/vista2/" >Ir a vista 2</a>
    <a href="http://127.0.0.1:8000/vista3/" >Ir a vista 3</a>
    <a href="http://127.0.0.1:8000/vista4/" >Ir a vista 4</a>

"""

    return HttpResponse(html)

def vista2(request):
    html="""
    <h1 style="color:brown">BIENVENIDO</h1>
    <h1> ESTÁS EN LA VISTA 2 </h1>
    <a href="/" >Ir a vista 1</a>
    <a href="http://127.0.0.1:8000/vista3/" >Ir a vista 3</a>
    <a href="http://127.0.0.1:8000/vista4/" >Ir a vista 4</a>

"""

    return HttpResponse(html)