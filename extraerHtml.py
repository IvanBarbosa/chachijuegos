# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os

maxPages = 20
codigo = ""

def plataforma(eleccion):
    global codigo
    plat = ''
    if (eleccion == '2'):
        plat = '-pc'
        codigo = "f1"
    elif (eleccion == '3'):
        plat = '-ps4'
        codigo = "f37"
    elif (eleccion == '4'):
        plat = '-ps3'
        codigo = "f2"
    elif (eleccion == '5'):
        plat = '-ps2'
        codigo = "f7"
    elif (eleccion == '6'):
        plat = '-xbox-one'
        codigo = "f38"
    elif (eleccion == '7'):
        plat = '-x360'
        codigo = "f4"
    elif (eleccion == '8'):
        plat = '-wiiu'
        codigo = "f35"
    elif (eleccion == '9'):
        plat = '-wii'
        codigo = "f3"
    elif (eleccion == '10'):
        plat = '-3ds'
        codigo = "f34"
    elif (eleccion == '11'):
        plat = '-ds'
        codigo = "f5"
    elif (eleccion == '12'):
        plat = '-psvita'
        codigo = "f36"
    elif (eleccion == '13'):
        plat = '-psp'
        codigo = "f6"
    elif (eleccion == '14'):
        plat = '-ios'
        codigo = "f9"
    elif (eleccion == '15'):
        plat = '-web'
        codigo = "f8"
    elif (eleccion == '16'):
        plat = '-android'
        codigo = "f32"
    else:
        codigo = "f0"

    return plat

def genero(eleccion):

    global codigo
    gen = ""

    if (eleccion == '2'):
        codigo += "f1"
        ger = "-accion"
    elif (eleccion == '3'):
        codigo += "f3"
        gen = "-aventura"
    elif (eleccion == '4'):
        codigo += "f9"
        gen = "-casual"
    elif (eleccion == '5'):
        codigo += "f10"
        gen = "-conduccion"
    elif (eleccion == '6'):
        codigo += "f6"
        gen = "-deportes"
    elif (eleccion == '7'):
        codigo += "f2"
        gen = "-estrategia"
    elif (eleccion == '8'):
        codigo += "f8"
        gen = "-mmo"
    elif (eleccion == '9'):
        codigo += "f7"
        gen = "-rol"
    elif (eleccion == '10'):
        codigo += "f5"
        gen = "-simulacion"
    elif (eleccion == '11'):
        codigo += "f4"
        gen = "-otros"
    else:
        codigo += "f0"

    return gen

def orden(eleccion):
    orde = ""

    if (eleccion == '1'):
        orde = "juegos-populares"
    elif (eleccion == '2'):
        orde = "fecha"
    elif (eleccion == '3'):
        orde = "lanzamientos"
    elif (eleccion == '4'):
        orde = "esperados"
    else:
        orde = "valoracion"
 
    return orde

def combinaciones(pla, gen, orde):
    pla = plataforma(pla)
    gen = genero(gen)
    orde = orden(orde)
    iniUrl = "http://www.3djuegos.com/novedades/juegos-generos/juegos" + pla + gen + "/"
    finUrl = codigo + "f0/" + orde

    extraerDatos(iniUrl, finUrl)

def extraerDatos(iniUrl, finUrl):    
    for i in range(1,maxPages):
        url = iniUrl + str(i-1) + finUrl
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

                if (plat != None):
                    plat = plat.getText()
                else:
                    plat = ""

                if (puntuacion != None):
                    puntuacion = puntuacion.getText()

                if (fecha != None):
                    fecha = fecha.getText()

                print titulo.encode("utf-8") + " " + descripcion.encode("utf-8") + " " + fecha.encode("utf-8") + " " + puntuacion.encode("utf-8") + " " + plat.encode("utf-8")


        else:
            break

def menu():
    os.system('cls')

    print "1. Todos"
    print "2. PC"
    print "3. PS4"
    print "4. PS3"
    print "5. PS2"
    print "6. XOne"
    print "7. X360"
    print "8. WiiU"
    print "9.Wii"
    print "10. 3DS"
    print "11. DS"
    print "12. Vita"
    print "13. PSP"
    print "14. iOS"
    print "15. Web"
    print "16. Android"
    plataforma = raw_input("Plataforma: ")
    os.system('cls')

    print "1. Todos"
    print "2. Acción"
    print "3. Aventura"
    print "4. Casual"
    print "5. Conducción"
    print "6. Deportes"
    print "7. Estrategia"
    print "8. MMO"
    print "9. Rol"
    print "10. Simulación"
    print "11. Otros"
    genero = raw_input("Genero: ")
    os.system('cls')

    print "1.Populares"
    print "2. Nuevas altas"
    print "3. A la venta"
    print "4. Más esperados"
    print "5. Valoración"
    orden = raw_input("Orden: ")
    os.system('cls')

    combinaciones(plataforma, genero, orden)


menu()
