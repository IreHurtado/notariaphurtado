from django.views.generic.base import TemplateView

class CompraventaView(TemplateView):
    template_name="escrituras/escrituras_compraventa.html"
    
class HipotecaView(TemplateView):
    template_name="escrituras/escrituras_hipoteca.html"
    
class MatrimonioView(TemplateView):
    template_name="escrituras/escrituras_matrimonio.html"
    
class PoderesView(TemplateView):
    template_name="escrituras/escrituras_poderes.html"
    
class SociedadesView(TemplateView):
    template_name="escrituras/escrituras_sociedades.html"