from django.urls import path
from .views import CarrinhoViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
	path('adicionar_item/<int:camiseta_id>/', CarrinhoViewSet.as_view({'post': 'adicionar_item'}), name='adicionar_item'),
	path('remover_item/<int:camiseta_id>/', CarrinhoViewSet.as_view({'post': 'remover_item'}), name='remover_item'),
	path('esvaziar/', CarrinhoViewSet.as_view({'post': 'esvaziar_carrinho'}), name='esvaziar_carrinho'),
	path('comprar/', CarrinhoViewSet.as_view({'post': 'comprar'}), name='comprar'),
]
