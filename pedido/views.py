from rest_framework import viewsets, status
from .models import Pedido
from .serializers import PedidoSerializer
from rest_framework.permissions import AllowAny

class PedidoViewSet(viewsets.ModelViewSet):
	permission_classes = [AllowAny]
	queryset = Pedido.objects.all()
	serializer_class = PedidoSerializer
