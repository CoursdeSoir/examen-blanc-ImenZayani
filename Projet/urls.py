from django.urls import path
from .views import ListeProjets, AjoutProjet, AdhererProjet

urlpatterns = [
    path('liste/', ListeProjets.as_view(), name='liste_projets'),
    path('ajout/', AjoutProjet.as_view(), name='ajout_projet'),
    path('adherer/<int:projet_id>/', AdhererProjet.as_view(), name='adherer_projet'),
]
