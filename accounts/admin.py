from django.contrib import admin

# Register your models here.

from .models import Account, Store

admin.site.register(Account)
admin.site.register(Store)