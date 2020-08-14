from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='Store Home'),
    path('getproductlist/<int:num_item>/<int:page>', views.getProuductItems, name="get item list"),
]