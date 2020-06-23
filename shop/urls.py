from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/<int:catalogl1_id>/', views.catalog, name='catalog'),
    path('catalog/<int:catalogl1_id>/<int:catalogl2_id>/', views.catalog, name='catalog'),
]