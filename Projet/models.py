from django.db import models
from Etudiant.models import Etudiant

class Projet(models.Model):
    besoin = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    effectif = models.IntegerField(default=0)
    type = models.CharField(max_length=1, choices=[('w', 'Web'), ('m', 'Mobile'), ('d', 'Desktop')])
    createur = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='createur_projets')

    def __str__(self):
        return f"Projet {self.id}"

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(besoin__gte=0), name='besoin_non_negatif')
        ]
        
class Developpeur(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date_adhesion = models.DateField(auto_now_add=True)
