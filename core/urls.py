from django.contrib.auth import views as auth_views
from django.urls import path

from core import views

urlpatterns = [
    path('login/', auth_views.login, name='auth.login'),
    path('logout/', auth_views.logout, name='auth.logout'),
    path('', views.index, name='core.index'),
    path('calendario/', views.calendario, name='core.calendario'),
    path(
        'marcacao/<int:ano>/<int:mes>/<int:dia>/',
        views.marcacao, name='core.marcacao'
    ),
    path('consultas/', views.consultas, name='core.consultas'),
    path('requisicao/<int:id>/', views.requisicao, name='core.requisicao'),
    path(
        'lista/<int:ano>/<int:mes>/<int:dia>/',
        views.lista, name='core.lista'
    ),
    path(
        'agenda_mes/', views.agenda_mes, name='core.agenda_mes'
    ),
    path(
        'agenda_closed/', views.agenda_closed, name='core.agenda_closed'
    ),
    path(
        'agenda/<int:ano>/<int:mes>/', views.agenda, name='core.agenda'
    ),
    path(
        'bloquear/<int:ano>/<int:mes>/<int:dia>/',
        views.bloquear, name='core.bloquear'
    ),
    path(
        'desbloquear/',
        views.desbloquear, name='core.desbloquear'
    )
]
