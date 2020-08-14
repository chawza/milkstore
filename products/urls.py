from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>', views.product_info, name='product info'),
    path('img/<int:product_id>', views.get_image, name='get image'),
]