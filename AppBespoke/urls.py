from django.urls import path

from AppBespoke import views


urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('bicicletas', views.bicicletas, name="Bicicletas"),
    path('vidriera', views.vidriera, name="Vidriera"),
    path('otros', views.otros, name="Otros"),
    path('partes', views.partes, name="Partes"),
    # path('busquedaPartes', views.busquedaPartes, name="BusquedaPartes"),
    path('buscar/', views.buscar),
    path('leerPartes', views.leerPartes, name="LeerPartes"),
    path('eliminarPartes/<partes_nombre>/', views.eliminarPartes, name="EliminarPartes"),
    path('editarPartes/<partes_nombre>/', views.editarPartes, name="EditarPartes"),
    
]
