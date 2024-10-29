from rest_framework import serializers
from catalogo import models


class CamisetaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "nome",
            "tamanho",
        )
        model = models.Camiseta
