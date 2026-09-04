from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tipos/', views.tipos, name='tipos'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('perfil/', views.perfil, name='perfil'),
    
    
]
