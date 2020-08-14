from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

#import model from other apps
from products.models import Product

# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def getProuductItems(request, num_item, page):
    first_item = 1 + num_item*(page-1)
    query_set = Product.objects.all()[first_item:first_item+num_item] #slice items only from first item of page until num_item from first item in page

    item_list = []
    for item in query_set:
        item_list.append(
            {
                "id" : item.pk,
                "name" : item.name,
                "brand" : item.store_id.storename,
                "price" : item.price,
                "thumbnail" : item.thumbnail,
            }
        )
    json = {}
    json['items'] = item_list
    return JsonResponse(json)

