from django.urls import path

from notaria.views import (
  
    VehicularesView,
    
)

app_name = "vehicular"

urlpatterns = [

    path("transferencia/", VehicularesView.as_view(), name="transferenciavehicular"),
    

]