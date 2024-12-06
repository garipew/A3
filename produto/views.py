from rest_framework import viewsets
from . import models
from rest_framework.permissions import AllowAny
from .serializers import CamisetaSerializer


class CamisetaViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = models.Camiseta.objects.all()
    serializer_class = CamisetaSerializer

# Create your views here.
