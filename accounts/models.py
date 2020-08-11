from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField()
    cardnumber = models.CharField(max_length=19)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Store(models.Model):
    storename = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.storename
