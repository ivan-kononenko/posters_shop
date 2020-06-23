from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import CategoryL1, CategoryL2

x = 10
x1 = x + x
y = 10
y1 = x + y
if x1 is y1:
    variable_a = True
else:
    variable_a = False


def index(request):
    return HttpResponse(variable_a)


def catalog(request, catalogl1_id, catalogl2_id=None):
    if catalogl2_id:
        cat = CategoryL2.objects.get(pk=catalogl2_id)
    else:
        cat = CategoryL1.objects.get(pk=catalogl1_id)
    return HttpResponse(f"{catalogl1_id} - {catalogl2_id}<br>{cat.name}")
