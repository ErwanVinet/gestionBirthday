from django.shortcuts import render, redirect, get_object_or_404
from .models import Invite, Logement
from .forms import InviteForm, LogementForm
# Create your views here.

def home(request):
    invites = Invite.objects.all()
    return(render(request, 'home.html', {'invites':invites}))

def home_logement(request):
    logements = Logement.objects.all()
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
    return(render(request, 'ajout_invite.html'))

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

def supprimer_invite(request, invite_id):
    invite = get_object_or_404(Invite, id=invite_id)
    invite.delete()
    return redirect('home')

def supprimer_logement(request, logement_id):
    logement = get_object_or_404(Logement, id=logement_id)
    logement.delete()
    return redirect('home')

def gerer_invites_logement(request, salle_id):
    logement = get_object_or_404(Logement, id=salle_id)
    invites = Invite.objects.all()  # Tous les invités disponibles

    if request.method == "POST":
        invites_selectionnes = request.POST.getlist('invites')  # Liste des invités sélectionnés
        #Logemenent.invite_set.set(invites_selectionnes)  # Met à jour les invités dans la salle
        for invite in invites_selectionnes:
            Invite.objects.filter(logement=logement).update(logement=None)  # Supprime les anciens
            Invite.objects.filter(id__in=invites_selectionnes).update(logement=logement)  
        return redirect('home')  # Redirige après modification

    return render(request, 'gerer_logement.html', {'logement': logement, 'invites': invites})
