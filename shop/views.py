from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

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

