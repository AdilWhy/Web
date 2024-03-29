from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    json = {'products': list(products.values())}
    return JsonResponse(json)

def categories_list(request):
    categories = Category.objects.all()
    json = {'categories': list(categories.values())}
    return JsonResponse(json)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    json = {'product': {
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active
    }}
    return JsonResponse(json)

def category_detail(request, id):
    category = Category.objects.get(id=id)
    json = {'category': {
        'name': category.name
    }}
    return JsonResponse(json)

def category_products(request, id):
    category = Category.objects.get(id=id)
    products = category.product_set.all()
    json = {'products': list(products.values())}
    return JsonResponse(json)