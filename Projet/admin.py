# Dans le fichier admin.py de l'application Projet
from django.contrib import admin
from .models import Projet
from .admin import ProjetAdmin, TypeListFilter

class TypeListFilter(admin.SimpleListFilter):
    title = 'Type'
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return (
            ('Web', 'Projet Web'),
            ('Mobile', 'Projet Mobile'),
            ('Desktop', 'Projet Desktop'),
            ('Manque_effectif', 'Projet sans effectif'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Web':
            return queryset.filter(type='w')
        elif self.value() == 'Mobile':
            return queryset.filter(type='m')
        elif self.value() == 'Desktop':
            return queryset.filter(type='d')
        elif self.value() == 'Manque_effectif':
            return queryset.filter(effectif=0)

class ProjetAdmin(admin.ModelAdmin):
    list_filter = (TypeListFilter,)

admin.site.register(Projet, ProjetAdmin)