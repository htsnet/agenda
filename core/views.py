from django.shortcuts import render, HttpResponse

# Create your views here.
from core.models import Evento


def evento(request, titulo_evento):
    try:
        registro = Evento.objects.get(titulo=titulo_evento)
        texto = '<h1>Evento {}<h1>'.format(registro.local)
    except Evento.DoesNotExist:
        texto = '<h1>Evento não localizado! Tente escrever novamente.<h1>'
    return HttpResponse(texto)