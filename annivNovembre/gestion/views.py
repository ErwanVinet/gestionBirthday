from django.shortcuts import render, redirect, get_object_or_404
from .models import Invite, Logement, Orga, Extras
from .forms import InviteForm, LogementForm, ExtrasForm
from django.db.models import Count, Sum, Q
# Create your views here.

def home(request):
    name = request.GET.get('name')  # Tri par défaut par nom
    orga_id = request.GET.get('orga')  # Récupère l'ID de l'orga sélectionnée
    sans_logement = request.GET.get('sans_logement')  # Vérifie si on filtre les invités sans logement

    invites = Invite.objects.all()  # Applique le tri

    if name:
        invites = invites.filter(Q(nom__icontains=name) | Q(prenom__icontains=name))

    if orga_id:  # Filtre par Orga si sélectionnée
        invites = invites.filter(orga_id=orga_id)

    if sans_logement:  # Filtre uniquement les invités qui n'ont pas de logement
        invites = invites.filter(logement__isnull=True)

    orgas = Orga.objects.all()  # Liste des orgas pour créer les boutons
    count = Invite.objects.all().count()
    return render(request, 'home.html', {'invites': invites, 'orgas': orgas, 'sans_logement': sans_logement, 'count':count})



def home_logement(request):
    logements = Logement.objects.annotate(nombre_invites=Count('dors'))
    return(render(request, 'home_logement.html', {'logements':logements}))

def ajout_invite(request):
    if request.method == 'POST':
        form = InviteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige après ajout
    else:
        form = InviteForm()

    return(render(request, 'ajouter_invite.html', {'form':form}))

def ajout_salle(request):
    if request.method == 'POST':
        form = LogementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige après ajout
    else:
        form = LogementForm()
    return(render(request, 'ajout_logement.html', {'form':form}))

def gestion(request):
    prix_logement = Logement.objects.aggregate(Sum('prix'))['prix__sum']
    logements = Logement.objects.all().values('nom', 'prix')

    extras_nourriture = Extras.objects.all().filter(extra_type='Nourriture')
    extras_boisson = Extras.objects.all().filter(extra_type='Boisson')
    extras_autres = Extras.objects.all().filter(extra_type='Autre')

    prix_nourriture = 0
    prix_boisson = 0
    prix_autre = 0

    for extra in extras_nourriture:
        prix_nourriture += extra.quantite * extra.prix
        extra.total = extra.quantite * extra.prix

    for extra in extras_boisson:
        prix_boisson += extra.quantite * extra.prix
        extra.total = extra.quantite * extra.prix

    for extra in extras_autres:
        extra.total = extra.quantite * extra.prix
        prix_autre+= extra.quantite * extra.prix
        

    extra_prix = prix_nourriture + prix_boisson + prix_autre
    budget = prix_logement + extra_prix
    return(render(request, 'gestion.html', {'budget':budget, 'prix_logement':prix_logement, 'logements':logements, 
                                            'extra_prix':extra_prix, 'prix_nourriture':prix_nourriture, 
                                            'prix_boisson':prix_boisson, 'prix_autre':prix_autre, 'nourriture':extras_nourriture, 'boisson':extras_boisson, 'autre':extras_autres}))




def modifier_invite(request, invite_id):
    invite = get_object_or_404(Invite, id=invite_id)
    if request.method == "POST":
        form = InviteForm(request.POST, instance=invite)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige après modification
    else:
        form = InviteForm(instance=invite)
    
    return render(request, 'modifier_invite.html', {'form': form})

def modifier_logement(request, logement_id):
    logement = get_object_or_404(Logement, id=logement_id)
    if request.method == "POST":
        form = LogementForm(request.POST, instance=logement)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige après modification
    else:
        form = LogementForm(instance=logement)
    
    return render(request, 'modifier_logement.html', {'form': form})

def supprimer_invite(request, invite_id):
    invite = get_object_or_404(Invite, id=invite_id)
    invite.delete()
    return redirect('home')

def supprimer_logement(request, logement_id):
    logement = get_object_or_404(Logement, id=logement_id)
    logement.delete()
    return redirect('home')

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Logement, Invite

def gerer_invites_logement(request, salle_id):
    name = request.GET.get("name", "").strip()
    delete = request.GET.get("delete")
    if delete:
        Invite.objects.filter(id=delete).update(logement=None)
    logement = get_object_or_404(Logement, id=salle_id)

    # Liste des invités qui ne sont PAS dans ce logement
    invites = Invite.objects.filter(logement=None)
    
    # Filtrer les invités par nom/prénom si une recherche est faite
    if name:
        invites = invites.filter(Q(nom__icontains=name) | Q(prenom__icontains=name))

    # Liste des invités qui SONT DÉJÀ dans ce logement
    loges = Invite.objects.filter(logement=logement)

    if request.method == "POST":
        invites_selectionnes = request.POST.getlist('invites')  # Récupère les IDs des invités sélectionnés
        
        # 🔹 **Mettre à jour les invités**
        # 1️⃣ Supprime les invités de ce logement s'ils n'ont pas été sélectionnés
        #Invite.objects.filter(logement=logement).exclude(id__in=invites_selectionnes).update(logement=None)

        # 2️⃣ Ajoute les invités sélectionnés au logement
        Invite.objects.filter(id__in=invites_selectionnes).update(logement=logement)

         #return redirect('gerer_invites_logement salle.id')  # Redirection après mise à jour

    return render(request, 'gerer_logement.html', {'logement': logement, 'invites': invites, 'loges': loges})


def home_extra(request):
    type = request.GET.get('type')
    extras = Extras.objects.all()

    if type:
        extras = extras.filter(extra_type=type)
    return render(request, 'home_extra.html', {'extras':extras})

def supprimer_extra(request, extra_id):
    extra = get_object_or_404(Extras, id=extra_id)
    extra.delete()
    return redirect('home')

def ajout_extra(request):
    if request.method == 'POST':
        form = ExtrasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige après ajout
    else:
        form = ExtrasForm()

    return(render(request, 'ajouter_extra.html', {'form':form}))


def modifier_extra(request, extra_id):
    extra = get_object_or_404(Extras, id=extra_id)
    if request.method == "POST":
        form = ExtrasForm(request.POST, instance=extra)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige après modification
    else:
        form = ExtrasForm(instance=extra)
    
    return render(request, 'modifier_extra.html', {'form': form})