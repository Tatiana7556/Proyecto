"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiProyecto.views import LG, actualizar, administrador, agregar,equipoSonido, estufa, estufaMabe, formularioCompra, formularioVenta, formulariopqr, informes, interfaz, lavadoraLG, lavadoraMabe, login, mabe, nevecon, neveraChallenger, neveraWhirlpool, portafolio, pqr, producto, productos, registro, televisor, televisorLG, televisores, terminos, whirlpool 
from MiProyecto.views import challenger, cotizaciones, electrodomesticos, equipoLG,tatiana,abba


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tatiana/',tatiana,),
    path('abba/',abba),
    path('administrador/',administrador),
    path('actualizar/',actualizar),
    path('agregar/',agregar),
    path('challenger/',challenger),
    path('cotizaciones/',cotizaciones),
    path('administrador/',administrador),
    path('electrodomesticos/',electrodomesticos),
    path('equipoLG/',equipoLG),
    path('equipoSonido/',equipoSonido),
    path('estufa/',estufa),
    path('estufaMabe/',estufaMabe),
    path('formularioCompra/',formularioCompra),
    path('formularioVneta/',formularioVenta),
    path('formulariopqr/',formulariopqr),
    path('informes/',informes),
    path('interfaz/',interfaz),
    path('lavadoraLG/',lavadoraLG),
    path('lavadoraMabe/',lavadoraMabe),
    path('LG/',LG),
    path('login/',login),
    path('mabe/',mabe),
    path('nevecon/',nevecon),
    path('neveraChallenger/',neveraChallenger),
    path('neveraWhirlpool/',neveraWhirlpool),
    path('portafolio/',portafolio),
    path('producto/',producto),
    path('productos/',productos),
    path('pqr/',pqr),
    path('registro/',registro),
    path('televisor/',televisor),
    path('televisorLG/',televisorLG),
    path('televisores/',televisores),
    path('terminos/',terminos),
    path('whirlpool/',whirlpool),

]  
