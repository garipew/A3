from django.http import HttpResponse
from django.template import loader
from .models import Camiseta

def catalogo(request):
    camisetas = Camiseta.objects.all().values()
    template = loader.get_template('todos_produtos.html')
    context = {
        'camisetas' : camisetas,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def servico(request):
  template = loader.get_template('servico.html')
  return HttpResponse(template.render())

def contato(request):
  template = loader.get_template('contato.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  return HttpResponse(template.render())

def detalhes(request, id):
  camiseta = Camiseta.objects.get(id=id)
  template = loader.get_template('detalhes.html')
  context = {
    'camiseta': camiseta,
  }
  return HttpResponse(template.render(context, request))
