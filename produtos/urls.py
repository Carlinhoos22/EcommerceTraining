from django.urls import path
from . import views
from produtos.views import ProdutoListView, ProdutoDetailView

app_name = "produtos"

urlpatterns = [
    path("", ProdutoListView.as_view(), name="principal"),
    path("detalhar/<int:id>", ProdutoDetailView.as_view(), name="detalhar_produto"),
]
