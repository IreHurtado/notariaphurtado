from django.urls import path

from notaria.views import (
  
    CompraventaView,
    HipotecaView,
    MatrimonioView,
    PoderesView,
    SociedadesView
    
    
)

app_name = "escrituras"

urlpatterns = [

    path("compraventa/", CompraventaView.as_view(), name="compraventa"),
    path("hipoteca/", HipotecaView.as_view(), name="hipoteca"),
    path("matrimonio/", MatrimonioView.as_view(), name="matrimonio"),
    path("poderes/", PoderesView.as_view(), name="poderes"),
    path("sociedades/", SociedadesView.as_view(), name="sociedades"),

]