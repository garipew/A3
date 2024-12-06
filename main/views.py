from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.routers import DefaultRouter
from django.urls import reverse
from carrinho.views import CarrinhoViewSet
from pedido.views import PedidoViewSet
from produto.views import CamisetaViewSet

class APIRootView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        base_url = f"{request.scheme}://{request.get_host()}"
        return Response({
            'message': 'Welcome to the API!',
            'routes': {
                'produtos': f'{base_url}/api/camiseta/',
                'carrinho': f'{base_url}/api/carrinho/',
                'pedidos': f'{base_url}/api/pedidos/',
            }
	})
