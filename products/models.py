import datetime

from django.db import models
from django.utils import timezone

from accounts.models import Store

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, default=0)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField()
    description = models.TextField(default='Product descriptions')
    thumbnail = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def was_added_recently(self):
        return self.date_add >= timezone.now() - datetime.timedelta(days=1)

    def buy(self, qty):
        num_item = self.quantity
        num_item -= qty
        if num_item >= 0:
            self.quantity = num_item
            self.save()
            return 'success'
        else:
            return 'to much value'

    def supply(self, qty):
        self.quantity += qty
        self.save()
        return 'success'
