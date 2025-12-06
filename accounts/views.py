from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import AccountUserChangeForm, AccountUserCreationForm

# --1 . Authentication Views--
class LoginView(auth_views.LoginView):
    """
    View de login customizada
    Aponta para o template 'accounts/login.html'
    """
    template_name = 'accounts/login.html'

class LogoutView(auth_views.LogoutView):
    """
    View de logout customizada
    Redireciona para a página de login após o logout
    """
    pass

def register(request):
    """
    View de Cadastro de usuário
    Cria um novo usuário e faz login automático após o cadastro
    """
    if request.method == 'POST':
        form = AccountUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Login automático após o cadastro
            # Redireciona para a página inicial após o cadastro
            return redirect('home')
    else:
        form = AccountUserCreationForm()

    context = {'form' : form}
    return render(request, 'accounts/register.html', context)

# --2 . Dashboard Views e Perfil --
@login_required
def dashboard(request):
    """
    View do Dashboard do usuário
    Apenas usuários autenticados podem acessar esta view.
    Exibe informações relevantes para o usuário autenticado
    """
    return render(request, 'accounts/dashboard.html')

@login_required
def edit_account(request):
    """
    View para editar o perfil do usuário
    Permite que o usuário atualize suas informações pessoais (Nome, e Email)
    """
    form = AccountUserChangeForm(
        instance=request.user,
        data=request.POST or None
    )

    if form.is_valid():
        form.save()
        messages.success(request, 'Dados atualizados com sucesso.')
        return redirect('accounts:dashboard')

    context = {'form': form}
    return render(request, 'accounts/edit_account.html', context)

@login_required
def edit_password(request):
    """
    View para alterar a senha do usuário
    Permite que o usuário altere sua senha atual
    """
    form = PasswordChangeForm(
        data=request.POST or None,
        user=request.user
    )

    if form.is_valid():
        form.save()
        messages.success(request, 'Senha alterada com sucesso.')
        # Ao alterar a senha, o usuário deve fazer login novamente
        return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/edit_password.html', context)
