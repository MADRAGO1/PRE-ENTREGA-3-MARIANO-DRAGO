from django.shortcuts import render
from django.http import HttpResponse
from EncMus.models import Musicos


# Create your views here.

def crea_musicos(req, nombre, apellido, instrumento, email, tel, edad, dni):
  
  nuevo_musico = Musicos (nombre=nombre, apellido=apellido, instrumento=instrumento, email=email, tel=tel, edad=edad, dni=dni)
  nuevo_musico.save()  

  return HttpResponse(f"""
    <p>Nombre: {nuevo_musico.nombre} - Apellido: {nuevo_musico.apellido} - Instrumento: {nuevo_musico.instrumento} - email: {nuevo_musico.email} - tel: {nuevo_musico.tel} - edad: {nuevo_musico.edad} - dni: {nuevo_musico.dni}
 """)

def lista_musicos(req):
  
  lista = Musicos.objects.all()

  return render(req, 'lista_musicos.html', {"lista_musicos": lista})

