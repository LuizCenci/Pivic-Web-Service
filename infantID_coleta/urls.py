from django.urls import path, include
from infantID_coleta.views import *

app_name = 'formulario'
urlpatterns = [
    path('/', include('infantID_coleta.urls')),
]
