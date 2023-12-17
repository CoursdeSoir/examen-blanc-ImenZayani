from django.shortcuts import render, redirect
from django.views import View
from .models import Projet

class ListeProjets(View):
    def get(self, request):
        projets = Projet.objects.all()
        return render(request, 'CouchePresentation/projet/liste.html', {'projets': projets})

class AjoutProjet(View):
    def get(self, request):
        return render(request, 'CouchePresentation/projet/ajout.html')

    def post(self, request):
        return redirect('liste_projets')

class AdhererProjet(View):
    def get(self, request, projet_id):
        projet = Projet.objects.get(id=projet_id)
        return render(request, 'CouchePresentation/projet/adherer.html', {'projet': projet})

    def post(self, request, projet_id):
        return redirect('liste_projets')