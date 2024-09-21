from django.db import models

# Create your models here.

class Musicos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    instrumento=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.CharField(max_length=50)
    edad=models.IntegerField()
    dni=models.CharField(max_length=50)

class Bandas(models.Model):
    nombre=models.CharField(max_length=50)
    Contacto=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.CharField(max_length=50)
    Estilo=models.CharField(max_length=50)
    Integrantes=models.IntegerField()

class Barandpubs(models.Model):
    nombre=models.CharField(max_length=50)
    Contacto=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.CharField(max_length=50)
    Estilo=models.CharField(max_length=50)
    dir=models.CharField(max_length=50)
    Sonidopropio=models.BooleanField()


class Salasensayo(models.Model):
    nombre=models.CharField(max_length=50)
    Contacto=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.CharField(max_length=50)
    Estilo=models.CharField(max_length=50)
    dir=models.CharField(max_length=50)
    cantsalas=models.IntegerField()

class Productores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    tel=models.CharField(max_length=50)
    