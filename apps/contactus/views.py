from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactRequestForm


def contactus_view(request):
    title = "Contact us"
    description = "Send us a message, dear customer"
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus/thanks')
    else:
        form = ContactRequestForm()

    return render(request, 'contactus.html', {'form': form, "title": title, "description": description})


def thanks_view(request):
    return render(request, 'thanks.html')



