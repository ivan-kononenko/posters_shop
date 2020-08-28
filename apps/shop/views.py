from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CategoryL1, CategoryL2, Product



def index(request):
    title = "Shop"
    category_list = CategoryL1.objects.all()
    return render(request, 'index.html', {"category_list": category_list, "title": title})


def category_l1_view(request, categoryl1_slug):
    current_category = CategoryL1.objects.get(slug=categoryl1_slug)
    child_categories = CategoryL2.objects.filter(parent=current_category.pk)
    title = current_category
    context = {
        "current_category": current_category,
        "child_categories": child_categories,
        "title": title
    }
    return render(request, 'category_l1.html', context)


def category_l2_view(request, categoryl1_slug, categoryl2_slug):
    current_category = CategoryL2.objects.get(slug=categoryl2_slug)
    products = Product.objects.filter(category=current_category.pk)
    title = current_category
    context = {
        "current_category": current_category,
        "products": products,
        "title": title
    }
    return render(request, 'category_l2.html', context)


def product_view(request, categoryl1_slug, categoryl2_slug, product_slug):
    current_product = Product.objects.get(slug=product_slug)
    title = current_product
    breadcrumbs = {
        "/": "home",
        "/shop/": "shop",
        current_product.category.parent.slug: current_product.category.parent.name,
        # current_product.category.name,
        "": current_product.name
    }
    context = {
        "current_product": current_product,
        "title": title,
        "breadcrumbs": breadcrumbs.items(),
    }
    return render(request, 'product.html', context)


