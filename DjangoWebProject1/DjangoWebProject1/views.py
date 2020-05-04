from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):
    p1 = Persona("Wilson Fabian", "Arenas Ortega")
    temas = ["Plantillas", "Modelos", "Formularios"]
    docExterno = loader.get_template('miPlantilla.html')       
    documento = docExterno.render({"nombre" : p1.nombre, "apellido" : p1.apellido, "temas" : temas})
    return HttpResponse(documento)

def saludo1(request):
    p1 = Persona("Wilson Fabian", "Arenas Ortega")
    temas = ["Plantillas", "Modelos", "Formularios"]
    nombre = "Fabian"
    apellido = "Arenas"
    docExterno = open("C:/Users/farenas/source/repos/DjangoWebProject1/DjangoWebProject1/DjangoWebProject1/Plantilla/miPlantilla.html")
    template = Template(docExterno.read())
    docExterno.close()
    ctx = Context({"nombre" : p1.nombre, "apellido" : p1.apellido, "temas" : temas})
    documento = template.render(ctx)
    return HttpResponse(documento)

def Fecha(request):
    fecha = datetime.datetime.now()
    documento = """
    <html>
        <body>
            <h1>Hora actual:  %s</h1>
        </body>
    </html>
    """ % fecha
    return HttpResponse(documento)

def Edad(request, anio, edad):
    fecha = datetime.datetime.now()
    edadActual = 18
    periodo = anio - 2020
    documento = """
    <html>
        <body>
            <h1>Edad actual:  %s y %s Edad: %s</h1>
        </body>
    </html>
    """ % (periodo, anio, edad)
    return HttpResponse(documento)