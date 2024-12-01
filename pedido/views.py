from rest_framework import viewsets, status
from .models import Pedido
from .serializers import PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
	queryset = Pedido.objects.all()
	serializer_class = PedidoSerializer
