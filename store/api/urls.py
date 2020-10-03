from django.urls import path

from . import views

urlpatterns = [
    path('list/<int:store_id>/', views.store_list, name='store list'),
    path('list/items/<int:store_id>/<int:num_page>/', views.store_item_list, name='item list by brand'),
]