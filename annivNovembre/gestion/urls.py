from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('ajout_invite/', views.ajout_invite, name='ajout_invite'),
    path('ajout_salle/', views.ajout_salle, name='ajout_salle'),
    path('gestion/', views.gestion, name='gestion'),
    path('modifier-invite/<int:invite_id>/', views.modifier_invite, name='modifier_invite'),
    path('supprimer-invite/<int:invite_id>/', views.supprimer_invite, name='supprimer_invite'),
    path('home_logement/', views.home_logement, name='home_logement'),
    path('supprimer-logement/<int:logement_id>/', views.supprimer_logement, name='supprimer_logement'),
    path('gerer-invites-salle/<int:salle_id>/', views.gerer_invites_logement, name='gerer_invites_logement'),
    path('modifier-logement/<int:logement_id>/', views.modifier_logement, name='modifier_logement'),
    path('home_extra/', views.home_extra, name='home_extra'),
    path('modifier-extra/<int:extra_id>/', views.modifier_extra, name='modifier_extra'),
    path('supprimer-extra/<int:extra_id>/', views.supprimer_extra, name='supprimer_extra'),
    path('ajout_extra/', views.ajout_extra, name='ajout_extra'),
]