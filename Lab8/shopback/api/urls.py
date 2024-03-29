from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('categories/', views.categories_list),
    path('products/<int:id>/', views.product_detail),
    path('categories/<int:id>/', views.category_detail),
    path('categories/<int:id>/products/', views.category_products),
]