from rest_framework import viewsets
from catalogo import models
from .serializers import CamisetaSerializer


class CamisetaViewSet(viewsets.ModelViewSet):
    queryset = models.Camiseta.objects.all()
    serializer_class = CamisetaSerializer
