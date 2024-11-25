from rest_framework import serializers
from .models import Carrinho, CarrinhoItem
from produto.models import Camiseta

class CarrinhoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrinhoItem
        fields = ['id', 'camiseta', 'quantidade', 'calcular_preco']

class CarrinhoSerializer(serializers.ModelSerializer):
    itens = CarrinhoItemSerializer(many=True, read_only=True)
    total_preco = serializers.ReadOnlyField(source='calcular_preco')

    class Meta:
        model = Carrinho
        fields = ['id', 'sessao', 'itens', 'total_preco']

