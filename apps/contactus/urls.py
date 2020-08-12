from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.contactus_view, name='contactus'),
    path('thanks/', views.thanks_view, name='thanks'),

]

urlpatterns += staticfiles_urlpatterns()