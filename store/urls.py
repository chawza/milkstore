from django.urls import path

from . import views

urlpatterns = [
    path('<int:account_id>', views.home, name='Store Home'),
]