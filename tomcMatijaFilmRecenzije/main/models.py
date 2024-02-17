from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def str(self):
        return self.user.username

class Film(models.Model):
    nazivFilma = models.CharField(max_length=100)
    redateljFilma = models.CharField(max_length=100)
    godinaIzlaska = models.IntegerField()
    zanr = models.CharField(max_length=100)
    preporukeFilma = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='preporuke')

    def __str__(self) -> str:
        return self.nazivFilma

    def Ocjena(self):
        avg_rating = self.recenzija_set.aggregate(models.Avg('ocjena'))['ocjena__avg']
        return round(avg_rating, 1) if avg_rating is not None else None

class Recenzija(models.Model):
    autorRecenzije = models.ForeignKey(User, on_delete=models.CASCADE)
    recenzija = models.TextField()
    ocjena = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.film.nazivFilma}/{self.autorRecenzije}"