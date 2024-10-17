from django.urls import path

from notaria.views import (
  
    CartasView,
    
)

app_name = "cartas"

urlpatterns = [

    path("notariales/", CartasView.as_view(), name="cartasnotariales"),
    

]