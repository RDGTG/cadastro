
from django.urls import path
from . import views


urlpatterns = [
    # Sua página inicial (home)
    path('', views.home, name='home'),
    
    # Rota para a página de cadastro
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    
    # Rota para a página de login
    path('login/', views.login, name='login'),
]


