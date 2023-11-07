from django.shortcuts import render
from produtos.models import Produto
from django.views.generic import ListView, DetailView


class ProdutoListView(ListView):
    model = Produto
    context_object_name = 'produtos'
    template_name = 'produtos/index.html'


class ProdutoDetailView(DetailView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'produtos/detalhar_produto.html'
    pk_url_kwarg = 'id'


#def produtos(request):
#    produtos = Produto.objects.filter(categoria__nome="Livro")
#    relogios = Produto.objects.filter(categoria__nome="Relogio")
#    return render(request, "produtos/index.html", {"produtos": produtos, "relogios": relogios})


#def detalhar_produtos(request, id):
#    product = Produto.objects.get(pk=id)
#    relogios = Produto.objects.filter(categoria__nome="Relogio").exclude(pk=id)
#    return render(request, "produtos/detalhar_produto.html", 
#                  {"produto": product,
#                   "relogios": relogios})