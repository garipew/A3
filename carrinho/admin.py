from django.contrib import admin
from .models import CarrinhoItem,Carrinho

# Register your models here.
class CarrinhoAdmin(admin.ModelAdmin):
   list_fields = ("itens",)
class CarrinhoItemAdmin(admin.ModelAdmin):
   list_fields = ("camiseta","quantidade", "calcular_preco",)
 
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(CarrinhoItem, CarrinhoItemAdmin)
