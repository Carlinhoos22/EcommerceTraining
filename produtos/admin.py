from django.contrib import admin
from produtos.models import Categoria, Produto, Product

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Product)
