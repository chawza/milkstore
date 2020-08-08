from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    date_create = models.DateField()

    def __str__(self):
        return self.username
