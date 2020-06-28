from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

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


def category_l1_view(request, categoryl1_id):
    current_category = CategoryL1.objects.get(pk=categoryl1_id)
    child_categories = CategoryL2.objects.filter(parent=categoryl1_id)
    context = {
        "current_category": current_category,
        "child_categories": child_categories
    }
    return render(request, 'shop/category_l1.html', context)


def category_l2_view(request, categoryl1_id, categoryl2_id):
    current_category = CategoryL1.objects.get(pk=categoryl1_id)
    products = Product.objects.filter(parent=categoryl2_id)
    context = {
        "current_category": current_category,
        "child_categories": child_categories
    }
    return render(request, 'shop/category_l1.html', context)
