from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer
from django.urls import reverse


@login_required
def profile(request):
    title = "Shop"
    customer = Customer.objects.get(user=request.user.id)
    breadcrumbs = {
        "/": "home",
        "": "profile",
    }
    return render(request, 'profile.html', {"customer": customer, "title": title, "breadcrumbs": breadcrumbs.items()})


