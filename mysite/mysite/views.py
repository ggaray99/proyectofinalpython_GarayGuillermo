from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def pagina_inicio(request):
    return HttpResponse("¡Bienvenido a la página de inicio!")

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("Hola Django - Coder")

def prueba_template(self):
    miHtml = open("C:/Users/ggaray/Desktop/Pre-Entrega 3/mysite/plantillas/template.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)