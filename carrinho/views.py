from rest_framework import viewsets, status
from rest_framework.response import Response
from produto.models import Camiseta
from .models import Carrinho, CarrinhoItem
from pedido.models import Pedido, PedidoItem
from .serializers import CarrinhoSerializer, CarrinhoItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class CarrinhoViewSet(viewsets.ViewSet):
	permission_classes = [IsAuthenticated]
	def list(self, request):
		carrinho,created = Carrinho.objects.get_or_create(dono=request.user)
		serializer = CarrinhoSerializer(carrinho)
		return Response(serializer.data)

	def adicionar_item(self, request, camiseta_id=None):
		if request.user.is_authenticated:
			camiseta = get_object_or_404(Camiseta, id=camiseta_id)
			carrinho,created = Carrinho.objects.get_or_create(dono=request.user)

			quantidade=0
			carrinho_item = None
			for item in carrinho.itens.all():
				if item.camiseta == camiseta:
					carrinho_item = item
					quantidade = carrinho_item.quantidade
					break
			adicionados=int(request.data['quantidade']) or 1
			quantidade+=adicionados
		
			if carrinho_item:
			    carrinho.itens.remove(carrinho_item)
			    
			carrinho_item, created = CarrinhoItem.objects.get_or_create(
			    camiseta=camiseta,
			    quantidade=quantidade
			)

			carrinho.itens.add(carrinho_item)

			return Response({'status': 'Item adicionado ao carrinho'})
		return Response({'status': 'Usuario nao autenticado'})

	def remover_item(self, request, camiseta_id=None):
		if request.user.is_authenticated:
			camiseta = get_object_or_404(Camiseta, id=camiseta_id)
			carrinho,created = Carrinho.objects.get_or_create(dono=request.user)

			carrinho_item = None
			for item in carrinho.itens.all():
				if item.camiseta == camiseta:
					carrinho_item = item
					break

			if carrinho_item:
				removidos = int(request.data['quantidade']) or 1
				nova_quantidade = carrinho_item.quantidade - removidos
				carrinho.itens.remove(carrinho_item)
				if(nova_quantidade > 0):
					novo_item, created = CarrinhoItem.objects.get_or_create(
							camiseta=camiseta,
							quantidade=nova_quantidade
							)
					carrinho.itens.add(novo_item)

			return Response({'status': 'Item removido do carrinho'})
		return Response({'status': 'Usuario nao autenticado'})

	def esvaziar_carrinho(self, request):
		if request.user.is_authenticated:
			carrinho,created = Carrinho.objects.get_or_create(dono=request.user)
			carrinho.itens.set({})
			return Response({'status': 'Carrinho esvaziado'})
		return Response({'status': 'Usuario nao autenticado'})

	def comprar(self, request):
		if request.user.is_authenticated:
			carrinho,created = Carrinho.objects.get_or_create(dono=request.user)
			pedido = Pedido.objects.create() 
			for item in carrinho.itens.all():
				pedidoItem,created = PedidoItem.objects.get_or_create(camiseta=item.camiseta, quantidade=item.quantidade)
				pedido.itens.add(pedidoItem)
			carrinho.itens.set({})
			return Response({'status': 'Compra realizada'})
		return Response({'status': 'Usuario nao autenticado'})
