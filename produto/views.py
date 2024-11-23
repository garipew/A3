from rest_framework import viewsets
from . import models
from .serializers import CamisetaSerializer


class CamisetaViewSet(viewsets.ModelViewSet):
    queryset = models.Camiseta.objects.all()
    serializer_class = CamisetaSerializer

# Create your views here.
