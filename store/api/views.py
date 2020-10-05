from django.http import request
from .serializers import ProductSerializer
from django.http import JsonResponse

from store.models import Store

def store_list(request):
    store_queries = Store.objects.all()
    store_list = {}
    store_list['stores'] = [{'id' : x.id, 'store_name' : x.storename} for x in store_queries]

    return JsonResponse(store_list)

def store_item_list(request, store_id, page):
    first_item = 0 + ((page-1)*20)
    item_list = Store.objects.get(id=store_id).product_set.all()[first_item:first_item+20]
    
    serializers = ProductSerializer(item_list, many=True)
    return JsonResponse({'items' : serializers.data}, safe=False)