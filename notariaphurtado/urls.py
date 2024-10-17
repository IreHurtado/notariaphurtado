
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from .views import contact_view, HomeView, NosotrosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("nosotros/", NosotrosView.as_view(), name="nosotros"),
    path("contacto/", contact_view, name="contacto"),
    path('escrituras/', include('notaria.urls.escrituras_url', namespace='escrituras')),
    path('autorizaciones/', include('notaria.urls.autorizaciones_url', namespace='autorizaciones')),
    path('cartas/', include('notaria.urls.cartas_url', namespace='cartas')),
    path('legalizaciones/', include('notaria.urls.legalizaciones_url', namespace='legalizaciones')),
    path('nocontencioso/', include('notaria.urls.nocontencioso_url', namespace='nocontencioso')),
    path('poderes/', include('notaria.urls.poderes_url', namespace='poderes')),
    path('vehicular/', include('notaria.urls.vehicular_url', namespace='vehicular')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]