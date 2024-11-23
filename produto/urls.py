from django.urls import path
from .views import CamisetaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("produtos", CamisetaViewSet, basename="produtos")
urlpatterns = router.urls
