from django.views.generic.base import TemplateView

class LegalizacionFirmaView(TemplateView):
    template_name="legalizaciones/legalizaciones_firmas.html"
    
class LegalizacionPjView(TemplateView):
    template_name="legalizaciones/legalizaciones_pj.html"

class LegalizacionPnView(TemplateView):
    template_name="legalizaciones/legalizaciones_pn.html"

class LegalizacionCopiasView(TemplateView):
    template_name="legalizaciones/legalizaciones_copias.html"