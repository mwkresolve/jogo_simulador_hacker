from django.shortcuts import render
from .models import Hardware

def hardware_detail(request):
    hardware = Hardware.objects.get(user=request.user)
    return render(request, 'hardware.html', {'hardware': hardware})
