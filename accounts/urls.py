from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_account, name='logout'),
    path('profile', views.profile_home, name='profile'),
    path('profile/edit', views.profile_edit, name='profile edit'),
    path('profile/delete', views.delete_account, name="delete account")
]