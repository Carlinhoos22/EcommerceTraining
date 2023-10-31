from django.shortcuts import render
from produtos.models import Produto
from django.views.generic import ListView
from produtos.models import Product


def produtos(request):
    produtos = Produto.objects.filter(categoria__nome="Livro")
    relogios = Produto.objects.filter(categoria__nome="Relogio")
    return render(request, "produtos/index.html", {"produtos": produtos, "relogios": relogios})


def detalhar_produtos(request, id):
    product = Produto.objects.get(pk=id)
    relogios = Produto.objects.filter(categoria__nome="Relogio").exclude(pk=id)
    return render(request, "produtos/detalhar_produto.html", 
                  {"produto": product,
                   "relogios": relogios})


class ProdutoListView(ListView):
    model = Product
    context_object_name = 'produtos'