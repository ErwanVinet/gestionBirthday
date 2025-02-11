from django import forms
from .models import Invite, Logement

class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['nom', 'prenom', 'orga']

class LogementForm(forms.ModelForm):
    class Meta:
        model = Logement
        fields = ['nom', 'localisation', 'lien', 'prix', 'place']
