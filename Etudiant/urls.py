from django.urls import path
from .views import ListeEtudiants  # Remplacez ListeEtudiants par votre vue réelle

urlpatterns = [
    path('liste/', ListeEtudiants.as_view(), name='liste_etudiants'),
    # Ajoutez d'autres URLs au besoin
]
