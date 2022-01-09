from django.urls import path
from django.urls.resolvers import URLPattern
from.import views

urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('registro',views.registro,name='registro'),# /nosotros
    path('consulta',views.consulta,name='consulta'),# /Consulta
]