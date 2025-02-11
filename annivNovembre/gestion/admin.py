from django.contrib import admin
from .models import Orga, Invite, Logemenent

# Enregistrement des modèles dans l'admin
admin.site.register(Orga)
admin.site.register(Invite)
admin.site.register(Logemenent)
