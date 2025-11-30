from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from .forms import AccountUserCreationForm

# View par login (Usamos a view nativa do Django)
class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

# View para logout (Usamos a view nativa do Django)
class LogoutView(auth_views.LogoutView):
    pass

# View para cadastro de usuário (Usamos uma view customizada)
def register(request):
    if request.method == 'POST':
        form = AccountUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário após o cadastro
            return redirect('home')  # Redireciona para a home após o cadastro
    else:
        form = AccountUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)
