from django.urls import path
from . import views

urlpatterns = [
    path('', views.Catalogo, name='catalogo_vinilo'),
    path('inicio', views.Catalogo, name='catalogo_vinilo'),
    path('contactanos', views.Contacto, name='contacto'),
    path('quienes-somos', views.QuienesSomos, name='quienes_somos'),
    path('solicitud', views.Solicitud, name='solicitud_vinilo'),
]