from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:id>/', views.article, name='article'),
    path('articles/create', views.create, name='create')
]
