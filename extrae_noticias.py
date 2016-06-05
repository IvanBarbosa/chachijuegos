# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os
import json

def getTitulo(url):
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:
        html = BeautifulSoup(req.text, 'html.parser')
        titulo = html.find('h1',{'class':'tit_arti_1 fftit3 c3b'})

        if(titulo != None):
            #Texto
            titulo = titulo.getText()

        else:
            #Video
            titulo = html.find('h1',{'class':'b fl '}).getText()

    return titulo

def extraerDatos():
    mensaje = {}
    url = "http://www.3djuegos.com/"
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:
        html = BeautifulSoup(req.text, 'html.parser')
        entradas = html.find_all('div',{'id':'zona_chapas_gfx'})
        referencia = entradas[0].find_all('div')
        imagen = entradas[0].find_all('img')

        for i in [0,1,2]:
            ref = format(referencia[i]['data-url'])
            img = format(imagen[i]['src'])
            titulo = getTitulo(ref)
            mensaje[i]=({'titulo': titulo, 'imagen':img,'referencia':ref})

    return mensaje


def extraerContenido(url):
    mensaje = {}
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:
        html = BeautifulSoup(req.text, 'html.parser')
        titulo = html.find('h1',{'class':'tit_arti_1 fftit3 c3b'})
        texto = html.find('p',{'class':'s16 b fftext c2 lh27'})
        video = html.find('meta',{'itemprop':'contentURL'})

        if(titulo != None):
            #Texto
            titulo = titulo.getText()
            texto = texto.getText()

        else:
            #Video
            titulo = html.find('h1',{'class':'b fl '}).getText()
            texto = html.find('div',{'class':'pr oh c3 lh16 a_n a_c7 a_c0h mar_rl52 s13 fftit'}).getText()
            video=format(video['content'])

        mensaje=({'texto': texto.encode("utf-8"),'video':video})
    return mensaje
