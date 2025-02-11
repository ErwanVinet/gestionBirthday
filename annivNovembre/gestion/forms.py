from django import forms
from .models import Invite, Logemenent

class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ['nom', 'prenom', 'orga']

class LogementForm(forms.ModelForm):
    class Meta:
        model = Logemenent
        fields = ['nom', 'localisation', 'lien', 'prix', 'place']
