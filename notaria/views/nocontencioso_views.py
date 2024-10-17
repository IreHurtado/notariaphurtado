from django.views.generic.base import TemplateView

class SucesionesView(TemplateView):
    template_name="nocontencioso/nocontencioso_sucesion.html"
    
class AdopcionView(TemplateView):
    template_name="nocontencioso/nocontencioso_adopcion.html"
    
class CeseunionView(TemplateView):
    template_name="nocontencioso/nocontencioso_ceseunion.html"
    
class DivorcioView(TemplateView):
    template_name="nocontencioso/nocontencioso_divorcio.html"
    
class PatrimoniofamiliarView(TemplateView):
    template_name="nocontencioso/nocontencioso_patrimoniof.html"
    
class UnionView(TemplateView):
    template_name="nocontencioso/nocontencioso_union.html"
    
class RectificacionView(TemplateView):
    template_name="nocontencioso/nocontencioso_rectificacion.html"