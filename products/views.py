from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Product

# Create your views here.
def index(request):
    latest_product_list = Product.objects.order_by('-date_add')[:5]
    context = {
        'latest_product_list' : latest_product_list,
    }
    return render(request, 'products/index.html', context)

def product_info(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExists:
        raise Http404("Product with id %s does not exists" % product_id)
    
    return render(request, 'products/product.html', {
        'product' : product,
        'thumbnail' : 'products/'+product.thumbnail,
    })