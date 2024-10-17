from django.urls import path

from notaria.views import (
  
    SucesionesView,
    AdopcionView,
    CeseunionView,
    DivorcioView,
    PatrimoniofamiliarView,
    UnionView,
    RectificacionView
)

app_name = "nocontencioso"

urlpatterns = [

    path("sucesiones/", SucesionesView.as_view(), name="sucesiones"),
    path("adopcion/", AdopcionView.as_view(), name="adopcion"),
    path("ceseunion/", CeseunionView.as_view(), name="ceseunion"),
    path("divorcio/", DivorcioView.as_view(), name="divorcio"),
    path("patrimoniofamiliar/", PatrimoniofamiliarView.as_view(), name="patrimoniofamiliar"),
    path("union/", UnionView.as_view(), name="union"),
    path("rectificacion/", RectificacionView.as_view(), name="rectificacion"),
    

]