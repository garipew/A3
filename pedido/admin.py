from django.contrib import admin
from .models import PedidoItem, Pedido

# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
	list_fields = ("status", "itens",)

class PedidoItemAdmin(admin.ModelAdmin):
	list_fields = ("camiseta", "quantidade","calcular_preco",)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoItem, PedidoItemAdmin)
