from django.contrib import admin
from django.urls import path
from core import views # importa as views do core

urlpatterns = [
    path('', views.home, name='home'), # rota para a página inicial
    path('admin/', admin.site.urls),
]
