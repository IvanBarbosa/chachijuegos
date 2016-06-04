# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os
import json

maxPages = 20
codigo = ""

def plataforma(eleccion):
    global codigo
    plat = ''
    if (eleccion == 'pc'):
        plat = '-pc'
        codigo = "f1"
    elif (eleccion == 'ps4'):
        plat = '-ps4'
        codigo = "f37"
    elif (eleccion == 'ps3'):
        plat = '-ps3'
        codigo = "f2"
    elif (eleccion == 'ps2'):
        plat = '-ps2'
        codigo = "f7"
    elif (eleccion == 'xbox-one'):
        plat = '-xbox-one'
        codigo = "f38"
    elif (eleccion == 'x360'):
        plat = '-x360'
        codigo = "f4"
    elif (eleccion == 'wiiu'):
        plat = '-wiiu'
        codigo = "f35"
    elif (eleccion == 'wii'):
        plat = '-wii'
        codigo = "f3"
    elif (eleccion == '3ds'):
        plat = '-3ds'
        codigo = "f34"
    elif (eleccion == 'ds'):
        plat = '-ds'
        codigo = "f5"
    elif (eleccion == 'psvita'):
        plat = '-psvita'
        codigo = "f36"
    elif (eleccion == 'psp'):
        plat = '-psp'
        codigo = "f6"
    elif (eleccion == 'ios'):
        plat = '-ios'
        codigo = "f9"
    elif (eleccion == 'web'):
        plat = '-web'
        codigo = "f8"
    elif (eleccion == 'android'):
        plat = '-android'
        codigo = "f32"
    else:
        codigo = "f0"

    return plat

def genero(eleccion):

    global codigo
    gen = ""

    if (eleccion == 'accion'):
        codigo += "f1"
        ger = "-accion"
    elif (eleccion == 'aventura'):
        codigo += "f3"
        gen = "-aventura"
    elif (eleccion == 'casual'):
        codigo += "f9"
        gen = "-casual"
    elif (eleccion == 'conduccion'):
        codigo += "f10"
        gen = "-conduccion"
    elif (eleccion == 'deportes'):
        codigo += "f6"
        gen = "-deportes"
    elif (eleccion == 'estrategia'):
        codigo += "f2"
        gen = "-estrategia"
    elif (eleccion == 'mmo'):
        codigo += "f8"
        gen = "-mmo"
    elif (eleccion == 'rol'):
        codigo += "f7"
        gen = "-rol"
    elif (eleccion == 'simulacion'):
        codigo += "f5"
        gen = "-simulacion"
    elif (eleccion == 'otros'):
        codigo += "f4"
        gen = "-otros"
    else:
        codigo += "f0"

    return gen

def combinaciones(pla, gen, orden):
    pla = plataforma(pla)
    gen = genero(gen)
    iniUrl = "http://www.3djuegos.com/novedades/juegos-generos/juegos" + pla + gen + "/"
    finUrl = codigo + "f0/" + orden

    mensaje = extraerDatos(iniUrl, finUrl)
    return mensaje

def extraerDatos(iniUrl, finUrl):
    mensaje = []
    for i in range(0,maxPages):
        url = iniUrl + str(i) + finUrl
        req = requests.get(url)
        statusCode = req.status_code

        if statusCode == 200:
            html = BeautifulSoup(req.text, 'html.parser')
            entradas = html.find_all('table',{'class':'tb100 fftit'})

            for i,entrada in enumerate(entradas):
                titulo = entrada.find('a', {'class' : 's18'}).getText()
                descripcion = entrada.find('p', {'class' : 's13 c4 mar_t6 mar_t4 lh17'}).getText()
                fecha = entrada.find('b')
                puntuacion = entrada.find('div', {'class' : 'val_cuadrado_gris fr mar_l16 mar_r2'})
                plat = entrada.find('span', {'class' : 'plats bg_c4c mar_r4 dib mar_t8'})
                imagen = entrada.find('img')
                imagen = format(imagen['src'])

                if (plat != None):
                    plat = plat.getText()
                else:
                    plat = ""

                if (puntuacion != None):
                    puntuacion = puntuacion.getText()

                if (fecha != None):
                    fecha = fecha.getText()

                mensaje.append({'titulo': titulo.encode("utf-8"), 'descripcion' : descripcion.encode("utf-8"), 'fecha': fecha.encode("utf-8"), 'puntuacion': puntuacion.encode("utf-8"), 'plataforma':plat.encode("utf-8"), 'imagen':imagen})
        else:
            break
    return mensaje
