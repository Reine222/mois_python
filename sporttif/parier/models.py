from django.db import models


# Create your models here.


class Formule(models.Model):
    nom = models.CharField(max_length=100)
    message = models.TextField(null=True)


class Meta:
    verbose_name = "Formule"


def __str__(self):
    return self.nom


class Client(models.Model):
    pseudo = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=128)
    sex = models.CharField(max_length=10)
    localisation = models.CharField(max_length=42)

    class Meta:
        verbose_name = "Client"

    def __str__(self):
        return self.pseudo
