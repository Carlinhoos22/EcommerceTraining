from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path("", views.login_cliente, name="login"),
    path("cadastrar/", views.cadastro_cliente, name="cadastro"),
    path("sair/", views.sair_cliente, name="logout"),
]
