from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.shop.models import Product


def main_view(request):
    title = "Main page"
    description = "From here you can proceed to the following pages:"
    products = Product.objects.all().order_by("?")[:3]
    content = {
        "title": title,
        "description": description,
        "products": products,
    }
    return render(request, 'main.html', content)


def feedback_view(request):
    title = "Feedback"
    return render(request, 'feedback.html', {"title": title})


def about_view(request):
    title = "About"
    return render(request, 'about.html', {"title": title})

