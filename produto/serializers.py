from rest_framework import serializers
from . import models


class CamisetaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "nome",
            "preco",
            "quantidade",
            "descricao",
            "img",
        )
        model = models.Camiseta
