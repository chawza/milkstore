import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    date_add = models.DateTimeField('date add in database')
    quantity = models.IntegerField('availabale in storage')
    thumbnail = models.CharField(max_length=32)

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
