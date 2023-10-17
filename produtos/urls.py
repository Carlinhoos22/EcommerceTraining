from django.urls import path
from . import views

app_name = "produtos"

urlpatterns = [
    path("", views.produtos, name="principal"),
    path("detalhar/<int:id>", views.detalhar_produtos, name="detalhar_produto"),
]