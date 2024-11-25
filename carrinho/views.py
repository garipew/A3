from rest_framework import viewsets, status
from rest_framework.response import Response
from produto.models import Camiseta
from .models import Carrinho, CarrinhoItem
from .serializers import CarrinhoSerializer, CarrinhoItemSerializer
from django.shortcuts import get_object_or_404

class CarrinhoViewSet(viewsets.ViewSet):
    def get_carrinho_sessao(self, request):
        if not request.session.session_key:
            request.session.create()
        sessao = request.session.session_key
        carrinho,created = Carrinho.objects.get_or_create(sessao=sessao)
        return carrinho

    def list(self, request):
        carrinho = self.get_carrinho_sessao(request)
        serializer = CarrinhoSerializer(carrinho)
        return Response(serializer.data)

    def create(self, request):
        carrinho = self.get_carrinho_sessao(request)
        serializer = CarrinhoSerializer(carrinho, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def adicionar_item(self, request, camiseta_id=None):
        camiseta = get_object_or_404(Camiseta, id=camiseta_id)
        carrinho = self.get_carrinho_sessao(request)

        carrinho_item, created = CarrinhoItem.objects.get_or_create(
            camiseta=camiseta,
            quantidade=1  
        )

        carrinho.itens.add(carrinho_item)

        return Response({'status': 'Item adicionado ao carrinho'})

