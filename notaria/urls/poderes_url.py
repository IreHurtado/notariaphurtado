from django.urls import path

from notaria.views import (
  
    PoderesfueraregistroView,
    
)

app_name = "poderes"

urlpatterns = [

    path("fueraderegistro/", PoderesfueraregistroView.as_view(), name="poderesfueraregistro"),
    

]