from django.urls import path, include
from . import views

urlpatterns = [
    path('polls/', views.index, name='polls'),
    path('admin/', views.index, name = 'index'),
]