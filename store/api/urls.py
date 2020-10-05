from django.urls import path

from . import views

urlpatterns = [
    path('store/', views.store_list, name='store list'),
    #path('store/<int:store_id>/', views.store, name='store description'),
    path('items/<int:store_id>/<int:page>/', views.store_item_list, name='item list by brand'),
]