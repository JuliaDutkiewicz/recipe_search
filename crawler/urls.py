from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log_in', views.log_in, name='log_in'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('search', views.search, name='search'),
    path('favorites', views.favorites, name='favorites'),
]