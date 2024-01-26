from django.shortcuts import render


def Home(request):
    return render(request, 'home.html')

def Nosotros(request):
    return render(request, 'nosotros.html')


def Equipo(request):
    return render(request, 'equipo.html')

