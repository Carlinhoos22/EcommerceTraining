from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib import messages


def login_cliente(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("password")
        user = authenticate(username=email, password=senha)
        if user:
            login(request, user)
            return redirect("produtos:principal")
        else:
            messages.info(request, "Dados Inválidos! Tente novamente")

    return render(request, "clientes/login.html")


def cadastro_cliente(request):
    if request.method == "POST":
        email = request.POST.get("email")
        passwd = request.POST.get("password")
        user_created = get_user_model().objects.create(email=email)
        user_created.set_password(passwd)
        user_created.save()

    return render(request, "clientes/cadastro.html")


def sair_cliente(request):
    logout(request)
    return redirect(reverse("produtos:principal"))
