from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render



def saludo(req):
    return HttpResponse("hOLA MARIANO")

def probando_template(self):

    nom = "Nicolas"

    ap = "Perez"

    listadenotas = [2,2,3,7,5]

    diccionario = {"nombre": nom, "apellido": ap, "notas": listadenotas}

    mi_html = open("C:/Users/Usuario/Documents/CODERHOUSE/PREENTREGA 3 MARIANO DRAGO/Proyecto1/Templates/template1.html")

    plantilla = Template(mi_html.read())    

    mi_html.close()
    mi_contexto = Context(diccionario)

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)

def lista_musicos(request):
    musicos = Musicos.objects.all()  # Reemplaza con tu consulta real
    print(musicos)  # Imprime los datos para verificar
    return render(request, 'enc_mus/lista_musicos.html', {'lista_musicos': musicos})


       
