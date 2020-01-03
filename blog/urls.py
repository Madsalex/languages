from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:id>/', views.article, name='article'),
    path('articles/create', views.create, name='create'),
    path('articles/', views.articles, name='article'),
    path('map/', views.map, name='map'),
    path('list/', views.view_entries, name='entries'),
]
