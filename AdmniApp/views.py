from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib import messages
from .models import Productos, Merma, Proveedor, ClientesVip, Servicios


def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Ajusta el nombre del destino
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

from django.contrib.auth.decorators import login_required

def dashboard(request):
    return render(request, 'dashboard.html')


from .models import Bitacora 

def bitacora_view(request):
    registros = Bitacora.objects.all().order_by('-fecha') 
    return render(request, 'bitacora.html', {'registros': registros})

def almacen_view(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'agregar':
            nombre = request.POST['nombre']
            cantidad = int(request.POST['cantidad'])
            precio_com = float(request.POST['precio_com'])
            precio_venta = float(request.POST['precio_venta'])
            categoria = request.POST['categoria']
            # ¡No obtenemos ni usamos fecha_ingreso!

            with connection.cursor() as cursor:
                cursor.callproc('AgregarProducto', [
    nombre, cantidad, precio_com, precio_venta, categoria
])

        elif accion == 'eliminar':
            id_producto = int(request.POST['id_producto'])
            with connection.cursor() as cursor:
                cursor.callproc('EliminarProducto', [id_producto])

        return redirect('almacen')

    # GET: mostrar productos
    productos = Productos.objects.all().order_by('id_producto')
    return render(request, 'almacen.html', {'productos': productos})



def merma_view(request):
    mermas = Merma.objects.all().order_by('-fecha')
    return render(request, 'merma.html', {'mermas': mermas})

def proveedores_view(request):
    proveedores = Proveedor.objects.all().order_by('nombre')
    return render(request, 'proveedores.html', {'proveedores': proveedores})

def clientes_view(request):
    clientes = ClientesVip.objects.all().order_by('-puntos')
    return render(request, 'clientes.html', {'clientes': clientes})

def servicios_view(request):
    servicios = Servicios.objects.all().order_by('nombre')
    return render(request, 'servicios.html', {'servicios': servicios})

from django.shortcuts import render, redirect
from django.db import connection


