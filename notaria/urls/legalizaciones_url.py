from django.urls import path

from notaria.views import (
  
    LegalizacionFirmaView,
    LegalizacionPjView,
    LegalizacionPnView,
    LegalizacionCopiasView,
    
)

app_name = "legalizaciones"

urlpatterns = [

    path("firma/", LegalizacionFirmaView.as_view(), name="firma"),
    path("personajuridica/", LegalizacionPjView.as_view(), name="pj"),
    path("personanatural/", LegalizacionPnView.as_view(), name="pn"),
    path("copias", LegalizacionCopiasView.as_view(), name="copias"),

]