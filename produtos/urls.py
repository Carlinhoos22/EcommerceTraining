from django.urls import path
from . import views
from produtos.views import ProdutoListView, ProdutoDetailView, CreateView

app_name = "produtos"

urlpatterns = [
    path("", views.produtos, name="principal"),
    path("detalhar/<int:id>", views.detalhar_produtos, name="detalhar_produto"),
    path('produto/listagem/', ProdutoListView.as_view()),
    path('produto/detalhes/<int:id>/', ProdutoDetailView.as_view(), name="detalhar"),
    path('produtos/criar/', CreateView.as_view()),
]
