from django.shortcuts import render
from core.models import Jogador

def user_log_view(request):
    jogador = request.user
    log = jogador.log

    if request.method == 'POST':
        registro = request.POST.get('registro')
        jogador.log = registro
        jogador.save()

    context = {
        'log': log
    }

    return render(request, 'log.html', context)
