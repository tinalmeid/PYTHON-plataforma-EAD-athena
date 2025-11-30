from django.shortcuts import render
from django.views.decorators.http import require_http_methods # Necessário para o decorator
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactCourseForm # Se esse arquivo não existir, o servidor quebrará aqui!

# 1. VIEW HOME (Onde o erro estava)
@require_http_methods(["GET"])
def home(request):
    return render(request, 'home.html')

# 2. VIEW CONTACT (Que estávamos configurando a URL)
@require_http_methods(["GET", "POST"])
def contact(request):
    form = ContactCourseForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Lógica de envio de e-mail (Simulação)
        send_mail(
            f'Contato via Simple MOOC - {name}',
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL]
        )

        # Recria formulário vazio e mensagem de sucesso
        form = ContactCourseForm()
        context = {
            'form': form,
            'success_message': 'Sua mensagem foi enviada com sucesso!'
        }
        return render(request, 'contact.html', context)

    context = {'form': form}
    return render(request, 'contact.html', context)
