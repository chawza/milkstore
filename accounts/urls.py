from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile_home, name='profile'),
    path('profile/edit', views.profile_edit, name='profile edit'),
]