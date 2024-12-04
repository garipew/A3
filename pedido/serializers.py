from rest_framework import serializers
from .models import Pedido, PedidoItem
from produto.models import Camiseta

class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = ['id', 'camiseta', 'quantidade', 'calcular_preco']

class PedidoSerializer(serializers.ModelSerializer):
    itens = PedidoItemSerializer(many=True, read_only=True)
    total_preco = serializers.ReadOnlyField(source='calcular_preco')

    class Meta:
        model = Pedido
        fields = ['id', 'status', 'itens', 'total_preco']


