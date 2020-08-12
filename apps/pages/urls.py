from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('about/', views.about_view, name='about')

]