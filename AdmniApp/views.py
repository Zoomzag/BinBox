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



# Vista para Merma
def merma_view(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')

        try:
            if accion == 'agregar':
                id_producto = request.POST.get('id_producto')
                cantidad = request.POST.get('cantidad')
                motivo = request.POST.get('motivo')
                fecha = request.POST.get('fecha')

                if not all([id_producto, cantidad, motivo, fecha]):
                    messages.error(request, "Todos los campos son requeridos")
                    return redirect('merma')

                with connection.cursor() as cursor:
                    cursor.callproc('AgregarMerma', [
                        int(id_producto),
                        int(cantidad),
                        motivo,
                        fecha
                    ])
                messages.success(request, "Merma registrada exitosamente")

            elif accion == 'eliminar':
                id_merma = request.POST.get('id_merma')
                if not id_merma:
                    messages.error(request, "ID de merma requerido")
                    return redirect('merma')

                with connection.cursor() as cursor:
                    cursor.callproc('EliminarMerma', [int(id_merma)])
                messages.success(request, "Merma eliminada exitosamente")

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

        return redirect('merma')

    mermas = Merma.objects.all().order_by('-fecha')
    return render(request, 'merma.html', {'mermas': mermas})

# Vista para Proveedores
def proveedores_view(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'agregar':
            nombre = request.POST['nombre']
            telefono = request.POST['telefono']
            correo = request.POST['correo']
            direccion = request.POST['direccion']

            with connection.cursor() as cursor:
                cursor.callproc('AgregarProveedor', [nombre, telefono, correo, direccion])

        elif accion == 'eliminar':
            id_proveedor = int(request.POST['id_proveedor'])
            with connection.cursor() as cursor:
                cursor.callproc('EliminarProveedor', [id_proveedor])

        return redirect('proveedores')

    proveedores = Proveedor.objects.all().order_by('nombre')
    return render(request, 'proveedores.html', {'proveedores': proveedores})

# Vista para Clientes VIP
def clientes_view(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'agregar':
            nombre = request.POST['nombre']
            correo = request.POST['correo']

            with connection.cursor() as cursor:
                cursor.callproc('AgregarClienteVIP', [nombre, correo])

        elif accion == 'eliminar':
            id_cliente = int(request.POST['id_cliente'])
            with connection.cursor() as cursor:
                cursor.callproc('EliminarClienteVIP', [id_cliente])

        return redirect('clientes')

    clientes = ClientesVip.objects.all().order_by('-puntos')
    return render(request, 'clientes.html', {'clientes': clientes})

# Vista para Servicios
def servicios_view(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')

        if accion == 'agregar':
            nombre = request.POST['nombre']
            precio = float(request.POST['precio'])
            descripcion = request.POST['descripcion']

            with connection.cursor() as cursor:
                cursor.callproc('AgregarServicio', [nombre, precio, descripcion])

        elif accion == 'eliminar':
            id_servicio = int(request.POST['id_servicio'])
            with connection.cursor() as cursor:
                cursor.callproc('EliminarServicio', [id_servicio])

        return redirect('servicios')

    servicios = Servicios.objects.all().order_by('nombre')
    return render(request, 'servicios.html', {'servicios': servicios})

from django.shortcuts import render, redirect
from django.db import connection


