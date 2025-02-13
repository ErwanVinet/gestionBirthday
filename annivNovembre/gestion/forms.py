from django import forms
from .models import Invite, Logement, Extras

class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['nom', 'prenom', 'orga']

class LogementForm(forms.ModelForm):
    class Meta:
        model = Logement
        fields = ['nom', 'localisation', 'lien', 'prix', 'place']

class ExtrasForm(forms.ModelForm):
    class Meta:
        model = Extras
        fields = ['extra_type', 'nom', 'description', 'prix', 'quantite']