from django.contrib import admin
from .models import Orga, Invite, Logement, Extras

# Enregistrement des modèles dans l'admin
admin.site.register(Orga)
admin.site.register(Invite)
admin.site.register(Logement)
admin.site.register(Extras)
