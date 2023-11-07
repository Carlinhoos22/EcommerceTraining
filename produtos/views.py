from typing import Any
from django.shortcuts import render
from produtos.models import Produto
from django.views.generic import ListView, DetailView


class ProdutoListView(ListView):
    queryset = Produto.objects.filter(categoria__nome="livro")
    context_object_name = 'produtos'
    template_name = 'produtos/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['relogios'] = Produto.objects.filter(categoria__nome="Relogio")
        return context


class ProdutoDetailView(DetailView):
    model = Produto
    context_object_name = 'produto'
    template_name = 'produtos/detalhar_produto.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        produto = self.get_object()
        context['relogios'] = Produto.objects.filter(categoria__nome=produto.categoria).exclude(pk=produto.pk)
        return context


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