from rest_framework import viewsets, status
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PedidoViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	def list(self, request):
		user = request.user
		pedidos = Pedido.objects.filter(dono=user)
		serializer = PedidoSerializer(pedidos, many=True)
		return Response(serializer.data)
