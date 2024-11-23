from django.contrib import admin
from .models import Camiseta

# Register your models here.
class CamisetaAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "quantidade", "descricao", "img")

admin.site.register(Camiseta, CamisetaAdmin)

# Register your models here.
