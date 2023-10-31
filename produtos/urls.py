from django.urls import path
from . import views
from produtos.views import ProdutoListView

app_name = "produtos"

urlpatterns = [
    path("", views.produtos, name="principal"),
    path("detalhar/<int:id>", views.detalhar_produtos, name="detalhar_produto"),
    path('testando/', ProdutoListView.as_view()),
]
