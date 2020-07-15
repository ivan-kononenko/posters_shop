from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactRequestForm


def contactus_view(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus/thanks')
    else:
        form = ContactRequestForm()

    return render(request, 'contactus/contactus.html', {'form': form})


def thanks_view(request):
    return render(request, 'contactus/thanks.html')



