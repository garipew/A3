from django.urls import path
from .views import CarrinhoViewSet
from produto.urls import router

router.register("carrinho", CarrinhoViewSet, basename="carrinho")
urlpatterns = router.urls
urlpatterns.append(path('carrinho/adicionar_item/<int:camiseta_id>/', CarrinhoViewSet.as_view({'post': 'adicionar_item'}), name='adicionar_item'))

