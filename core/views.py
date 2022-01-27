from django.shortcuts import render, redirect
from django.views.decorators import csrf
from rest_framework.serializers import Serializer
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

def home(request):
    nombre= 'Claudia Andrea'

    vehiculos = Vehiculo.objects.all()

    return render(request, 'home.html', context={'nom_usuario': nombre, 'datos': vehiculos}
    )

def crearVehiculo(request):
    if request.method=='POST': 
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()
            return redirect('home')
    else:
        vehiculo_form= VehiculoForm()
    return render(request, 'core/form_crearvehiculo.html', {'vehiculo_form': vehiculo_form})


def Ver(request):
    vehiculos = Vehiculo.objects.all()

    return render(request, 'core/ver.html', context={'vehiculos':vehiculos})


def form_mod_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)

    datos ={
        'form': VehiculoForm(instance=vehiculo)
    }
    if request.method == 'POST': 
        formulario = VehiculoForm(data=request.POST, instance = vehiculo)
        if formulario.is_valid: 
            formulario.save()          
            return redirect('ver')
    return render(request, 'core/form_mod_vehiculo.html', datos)


def form_del_vehiculo(request,id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect('ver')




'''serializers'''
from rest_framework.serializers import Serializer
from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import VehiculoSerializer

@csrf_exempt
@api_view(['GET', 'POST'])



def lista_vehiculos(request): 
    if request.method== 'GET':
        vehiculo = Vehiculo.objects.all()
        serializer =VehiculoSerializer(vehiculo, many=True)
        return Response(serializer.data)

    elif request.method=='POST': 
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def lista_api(request):
    return render(request, 'ApiWeb.html')





   

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_vehiculo(request,id): 
    try: 
        vehiculo = Vehiculo.objects.get(patente=id) 
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET': 
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)
    if request.method=='PUT': 
        data = JSONParser().parse(request)
        serializer = VehiculoSerializer(vehiculo, data = data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE': 
        vehiculo.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

def nosotros(request):
    return render(request, "nosotros.html")

def entrada(request):
    return render(request, "entrada.html")

def blog(request):
    return render(request, "blog.html")

def anuncios(request):
    return render(request, "anuncios.html")

def anuncio(request):
    return render(request, "anuncio.html")

def Contacto(request):
    return render(request, "contacto.html")

def login(request):
    return render(request, "login.html")