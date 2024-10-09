from django.http import HttpResponse
from django.template import loader

def catalogo(request):
    template = loader.get_template('produto.html')
    return HttpResponse(template.render())

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
