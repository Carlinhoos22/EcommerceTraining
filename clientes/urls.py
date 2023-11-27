from django.urls import path
from . import views
from clientes.views import UserCreateView, UserLoginView, UserUpdateView

app_name = "clientes"

urlpatterns = [
    path("", UserLoginView.as_view(), name="login"),
    path('<int:pk>/atualizar', UserUpdateView.as_view(), name='atualizar_cliente'),
    path("cadastrar/", UserCreateView.as_view(), name="cadastro"),
    path("sair/", views.sair_cliente, name="logout"),
]
