from django.contrib import admin
from django.urls import path
from core import views # importa as views do core
from django.urls import include, path # importa include para incluir URLs de outros apps
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'), # rota para a página inicial
    path('courses/', include('courses.urls', namespace='courses')), # inclui as URLs do app courses
    path('admin/', admin.site.urls),
]

#Configuração para servir imagens em modo de desenvolvimento (Media files)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

