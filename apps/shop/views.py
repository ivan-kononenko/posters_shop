from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CategoryL1, CategoryL2, Product



def index(request):
    category_list = CategoryL1.objects.all()
    return render(request, 'index.html', {"category_list": category_list})


def category_l1_view(request, categoryl1_id):
    current_category = CategoryL1.objects.get(pk=categoryl1_id)
    child_categories = CategoryL2.objects.filter(parent=categoryl1_id)
    context = {
        "current_category": current_category,
        "child_categories": child_categories
    }
    return render(request, 'category_l1.html', context)


def category_l2_view(request, categoryl1_id, categoryl2_id):
    current_category = CategoryL2.objects.get(pk=categoryl2_id)
    products = Product.objects.filter(category=categoryl2_id)
    context = {
        "current_category": current_category,
        "products": products
    }
    return render(request, 'category_l2.html', context)


def product_view(request, categoryl1_id, categoryl2_id, product_id):
    current_product = Product.objects.get(pk=product_id)
    context = {
        "current_product": current_product,
    }
    return render(request, 'product.html', context)


