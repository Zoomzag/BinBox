from django.contrib import admin
from django.urls import path
from . import views  # o desde donde tengas tu vista login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'), 
    path('almacen/', views.almacen_view, name='almacen'),
    path('merma/', views.merma_view, name='merma'),
    path('proveedores/', views.proveedores_view, name='proveedores'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('servicios/', views.servicios_view, name='servicios'),
    path('bitacora/', views.bitacora_view, name='bitacora'),
]