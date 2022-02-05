from django.db import models
from django.urls import reverse

class Autore(models.Model):

    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    nazione = models.CharField(max_length=50)

    def __str__(self):
        return self.nome+" "+self.cognome
    def get_absolute_url(self):
        return reverse("autori", kwargs={"id": self.id})    

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

class Genere(models.Model):

    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Articolo(models.Model):

    titolo = models.CharField(max_length=50)
    testo = models.TextField(max_length=200)
    autore = models.ForeignKey(Autore, null=True, on_delete=models.CASCADE, related_name="articoli")
    genere = models.ManyToManyField(Genere)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
