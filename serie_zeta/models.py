from django.db import models

class Squadra(models.Model):
    nome = models.CharField(max_length=50)
    colore_divisa = models.CharField(max_length=50)
    num_max_giocatori = models.IntegerField()

    def __str__(self):
        return self.nome

class Torneo(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    data_inizio = models.DateField()
    data_fine = models.DateField()
    squadre = models.ManyToManyField(Squadra)

    def __str__(self):
        return self.nome

