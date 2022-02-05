from django.db import models

class Autore(models.Model):

    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    nazione = models.CharField(max_length=50)

    def __str__(self):
        return self.nome+" "+self.cognome

class Genere(models.Model):

    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Articolo(models.Model):

    titolo = models.CharField(max_length=50)
    testo = models.TextField(max_length=200)
    autore = models.ForeignKey(Autore, null=True, on_delete=models.CASCADE)
    genere = models.ManyToManyField(Genere)

    def __str__(self):
        return self.titolo
