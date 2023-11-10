from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib import messages
from django.views.generic import CreateView
from clientes.forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


# def login_cliente(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         senha = request.POST.get("password")
#         user = authenticate(username=email, password=senha)
#         if user:
#             login(request, user)
#             return redirect("produtos:principal")
#         else:
#             messages.info(request, "Dados Inválidos! Tente novamente")

#     return render(request, "clientes/login.html")


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'clientes/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('/')

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.error(self.request, "USUÁRIO OU SENHA INVÁLIDOS!")
        return super().form_invalid(form)
    

class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'clientes/cadastro.html'
    success_url = '/'
    success_message = "Usuário Criado Com Sucesso!"

# def cadastro_cliente(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         passwd = request.POST.get("password")
#         user_created = get_user_model().objects.create(email=email)
#         user_created.set_password(passwd)
#         user_created.save()

#     return render(request, "clientes/cadastro.html")


def sair_cliente(request):
    logout(request)
    return redirect(reverse("produtos:principal"))
