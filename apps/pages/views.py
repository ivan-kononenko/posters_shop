from django.shortcuts import render
from django.http import HttpResponseRedirect


def main_view(request):
    title = "Main page"
    description = "From here you can proceed to the following pages:"
    return render(request, 'main.html',  {"title": title, "description": description})


def feedback_view(request):
    title = "Feedback"
    return render(request, 'feedback.html', {"title": title})


def about_view(request):
    return render(request, 'about.html')
