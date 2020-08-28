from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:categoryl1_slug>/', views.category_l1_view, name='categoryl1'),
    path('<str:categoryl1_slug>/<str:categoryl2_slug>/', views.category_l2_view, name='categoryl2'),
    path('<str:categoryl1_slug>/<str:categoryl2_slug>/<str:product_slug>/', views.product_view, name='product'),

]
