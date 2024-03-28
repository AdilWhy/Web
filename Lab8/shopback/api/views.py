from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    json = {'products': list(products.values())}
    return JsonResponse(json)
