from django.urls import path
from . import views
from clientes.views import UserCreateView, UserLoginView

app_name = "clientes"

urlpatterns = [
    path("", UserLoginView.as_view(), name="login"),
    path("cadastrar/", UserCreateView.as_view(), name="cadastro"),
    path("sair/", views.sair_cliente, name="logout"),
]
