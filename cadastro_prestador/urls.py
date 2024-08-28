
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_cadastro.urls')),
    path('admin/', admin.site.urls),
    path('app_cadastro/', include('app_cadastro.urls')),  # Inclui as URLs do seu app
    
]
