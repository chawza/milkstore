from django.contrib import admin

# Register your models here.

from .models import Store, UserDetail

admin.site.register(Store)
admin.site.register(UserDetail)