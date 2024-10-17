from django.urls import path

from notaria.views import (
  
    AutorizacionesView,
    
)

app_name = "autorizaciones"

urlpatterns = [

    path("viaje/", AutorizacionesView.as_view(), name="viaje"),
    

]