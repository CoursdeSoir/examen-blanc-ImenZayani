from django.shortcuts import render
from django.views import View
from .models import Etudiant

class ListeEtudiants(View):
    def get(self, request):
        etudiants = Etudiant.objects.all()
        return render(request, 'CouchePresentation/etudiant/liste.html', {'etudiants': etudiants})
