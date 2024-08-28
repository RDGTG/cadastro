
from django.shortcuts import render, redirect
from .forms import CadastroForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib import messages
from django.core.mail import send_mail
from .forms import LoginForm
# Create your views here.

def home(request):
    # Renderiza a página inicial
    return render(request, 'home.html')

def cadastrar(request):
    if request.method == 'POST':  # 'POST' deve estar em maiúsculas
        form = CadastroForm(request.POST)  # 'POST' deve estar em maiúsculas
        if form.is_valid():
            form.save()
            return redirect('home')  # Use o nome da rota, não o template
        
    else:
        form = CadastroForm()
    return render(request, 'cadastrar.html', {'form': form})  # Corrija a sintaxe para dicionário


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get("nome")
            senha = form.cleaned_data.get("senha")
            print(f"Nome: {nome}, Senha: {senha}")
            user = authenticate(request, username=nome, password=senha)
            if user:
                login_django(request, user)  # Autentica o usuário na sessão
                messages.success(request, 'Login bem-sucedido!')  # Mensagem de sucesso
                
                # Enviar e-mail com informações do usuário
                subject = 'Novo login realizado'
                message = f'Usuário {user.username} realizou login com sucesso.'
                from_email = 'trodrigo350@gmail.com'
                recipient_list = ['gerencia@gmail.com']
                send_mail(subject, message, from_email, recipient_list)
                
                return redirect('home')  # Redireciona para a página inicial       
            else:
                messages.error(request, 'Usuário ou senha inválidos.')          
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})