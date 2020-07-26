from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]