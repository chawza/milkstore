from django.db import models
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Transaction(models.Model):
    customer = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    item = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return 'transaction {} on {}'.format(self.pk, self.date)