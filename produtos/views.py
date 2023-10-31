from django.shortcuts import render
from produtos.models import Produto
from django.views.generic import ListView, DetailView, CreateView
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
    template_name = 'produtos/product_list.html'


class ProdutoDetailView(DetailView):
    model = Product
    context_object_name = 'produto'
    template_name = 'produtos/detalhes.html'
    pk_url_kwarg = 'id'


class ProdutoCreateView(CreateView):
    model = Product
    fields = ('name', 'description')
    success_url = "/"