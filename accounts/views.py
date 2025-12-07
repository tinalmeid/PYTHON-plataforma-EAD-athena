from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import AccountUserCreationForm, AccountUserChangeForm

# --- 1. AUTENTICAÇÃO ---

class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(auth_views.LogoutView):
    pass

@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        form = AccountUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = AccountUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

# --- 2. DASHBOARD (Adicionando a segurança que falta) ---

@login_required
@require_http_methods(["GET"]) # <--- ADICIONE ISTO AQUI (Para o Sonar)
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
@require_http_methods(["GET", "POST"]) # <--- E ISTO AQUI
def edit_account(request):
    form = AccountUserChangeForm(instance=request.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Dados atualizados com sucesso!')
        return redirect('accounts:dashboard')
    context = {'form': form}
    return render(request, 'accounts/edit_account.html', context)

@login_required
@require_http_methods(["GET", "POST"]) # <--- E ISTO AQUI TAMBÉM
def edit_password(request):
    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, 'Senha alterada com sucesso!')
        return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/edit_password.html', context)
