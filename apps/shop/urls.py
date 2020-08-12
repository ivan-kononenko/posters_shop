from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:categoryl1_id>/', views.category_l1_view, name='categoryl1'),
    path('<int:categoryl1_id>/<int:categoryl2_id>/', views.category_l2_view, name='categoryl2'),
    path('<int:categoryl1_id>/<int:categoryl2_id>/<int:product_id>/', views.product_view, name='product'),

]
