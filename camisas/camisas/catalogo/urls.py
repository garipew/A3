from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.main, name='main'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('servico/', views.servico, name='servico'),
    path('contato/', views.contato, name='contato'),
    path('testing/', views.testing, name='testing'),
]
