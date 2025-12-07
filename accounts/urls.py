from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('editar/', views.edit_account, name='edit_account'),
    path('editar-senha/', views.edit_password, name='edit_password'),
]
