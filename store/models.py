from django.db import models
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import Account, Store
# Create your models here.

class Transaction(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=0)
    amount = models.IntegerField()
    payment = models.CharField(max_length=255, default="DEBIT")
    customer_address = models.CharField(max_length=255, default='')
    items = models.TextField(default='') #will store json file as strings. each pk will have the item amount
    store_address = models.CharField(max_length=255, default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'transaction {} on {}'.format(self.pk, self.date)