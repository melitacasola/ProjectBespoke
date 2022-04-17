from urllib.request import Request
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from AppBespoke.models import Bicicleta, Partes, Vidriera, Otros

from AppBespoke.forms import PartesFormulario

# Create your views here.

def inicio(request):
    
    return render(request, "AppBespoke/inicio.html")

def bicicletas(request):
    
    return render(request, "AppBespoke/bicicletas.html")

def vidriera(request):

    return render(request, "AppBespoke/vidriera.html")

def otros(request):
    return render(request, "AppBespoke/otros.html")


def partes(request):
    
    if request.method == 'POST':

        miFormulario = PartesFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

                informacion = miFormulario.cleaned_data
                
                producto = Partes (nombre=informacion['nombre'], stock=informacion['stock'], pedido=informacion['pedido']) 

                producto.save()

                return render(request, "AppBespoke/inicio.html") #Vuelvo al inicio o a donde quieran

    else: 

        miFormulario= PartesFormulario() #Formulario vacio para construir el html

    return render(request, "AppBespoke/partes.html", {"miFormulario":miFormulario})


def busquedaPartes(request):
    return render(request, "AppBespoke/busquedaPartes.html")


def buscar(request):

    if  request.GET["nombre"]:

	    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
        nombre = request.GET['nombre'] 
        partes = Partes.objects.filter(nombre__icontains=nombre)

        return render(request, "AppBespoke/resultadoBusqueda.html", {"nombre":nombre})

    else: 

	    respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)


def leerPartes(request):
    
    partes = Partes.objects.all() #trae todo los profesores
    
    contexto= {"partes": partes}
    
    return render(request, "AppBespoke/leerPartes.html", contexto)


def eliminarPartes(request, partes_nombre):
    
    partes = Partes.objects.get(nombre=partes_nombre)
    partes.delete()
    
    #vuelvo al menu
    partes = Partes.objects.all() #traemos todos
    
    contexto= {"partes":partes}
    
    return render(request, "AppBespoke/leerPartes.html", contexto)


def editarPartes(request, partes_nombre):
    
    #Recibe el nombre del profesor que vamos a modificar
    partes = Partes.objects.get(nombre=partes_nombre)
    
    #Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        
        miFormulario = PartesFormulario(request.POST) #aquí mellega toda la información del html
        
        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data
            
            partes.nombre = informacion['nombre']
            partes.stock = informacion['stock']
            partes.pedido = informacion['pedido']
                       
            partes.save()

            return render(request, "AppBespoke/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
    else: 
        
        #Creo el formulario con los datos que voy a modificar
        miFormulario= PartesFormulario(initial={'nombre': partes.nombre, 'stock':partes.stock , 'pedido':partes.pedido}) 
        
        #Voy al html que me permite editar
    return render(request, "AppBespoke/editarPartes.html", {"miFormulario":miFormulario, "partes_nombre":partes_nombre})
