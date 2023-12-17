from django.db import models
from django.contrib.auth.models import User

def Verif_username(value):
    if not value.startswith('ing'):
        raise models.ValidationError("Le nom d'utilisateur doit commencer par 'ing'.")

class Etudiant(User):
    classe = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username

    class Meta:
        unique_together = ['username']

    def Verif_username(self):
        if not self.username.startswith('ing'):
            raise ValidationError("Le nom d'utilisateur doit commencer par 'ing'.")
