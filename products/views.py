from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Product

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>hello world!</h1>")

def product_detail_view(request, id ):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse(f"product id {obj.content}")