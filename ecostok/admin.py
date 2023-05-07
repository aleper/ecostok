from django.contrib import admin

# Register your models here.

from ecostok.models import Material, Caixa, Coletor, Compra, Funcionario, Cliente, Venda, Preco_compra, Preco_venda

admin.site.register(Material)
admin.site.register(Caixa)
admin.site.register(Coletor)
admin.site.register(Compra)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Venda)
admin.site.register(Preco_compra)
admin.site.register(Preco_venda)

