from django.http import HttpResponse
import datetime

def saludo(request):
    documento = """
    <html>
        <body>
            <h1>Hello world!</h1>
        </body>
    </html>
    """
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
    edadActual  = 18
    periodo = anio - 2020
    documento = """
    <html>
        <body>
            <h1>Edad actual:  %s y %s Edad: %s</h1>
        </body>
    </html>
    """ % (periodo, anio, edad)
    return HttpResponse(documento)