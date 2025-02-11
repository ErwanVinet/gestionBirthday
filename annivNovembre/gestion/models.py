from django.db import models

# Create your models here.

class Orga(models.Model): 
    nom = models.CharField(max_length=15)
    #friends = models.ManyToManyField('Invite', blank=True, related_name='friend_of')  # Liste d'amis
    def __str__(self):
        return f"{self.nom}"


class Invite(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    orga = models.ForeignKey(Orga, on_delete=models.CASCADE, related_name='invites')
    logement = models.ForeignKey('Logement', null=True, on_delete=models.CASCADE, related_name='dors')
    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Logement(models.Model):
    nom = models.CharField(max_length=50)
    localisation = models.CharField(max_length=200)
    lien = models.URLField()
    prix = models.IntegerField()
    #loges = models.ManyToManyField('Invite', blank=True, related_name='loge')
    place = models.IntegerField()
    def __str__(self):
        return f"{self.nom}"