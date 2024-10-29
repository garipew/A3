from django.urls import path
from .views import CamisetaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", CamisetaViewSet, basename="catalogo")
urlpatterns = router.urls
