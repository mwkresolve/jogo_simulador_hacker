from django.shortcuts import render
from .models import Software

def user_software_view(request):
    # Obtenha os softwares do usuário (substitua 'user' pelo seu mecanismo de obtenção do usuário atual)
    user_softwares = Software.objects.filter(user=request.user)

    context = {
        'user_softwares': user_softwares
    }

    return render(request, 'software.html', context)
