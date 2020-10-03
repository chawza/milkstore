from products.models import Product
from rest_framework import serializers

from products.models import Product

class storeSerializer(serializers.Serializer):
    class Meta:
        model=Product
        fields = ['name', 'store_id', 'price', 'quantity', 'description', 'thumbnail']
