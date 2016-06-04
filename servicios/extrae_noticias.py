# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os
import json

def extraerDatos():  
    mensaje = {}  
    url = "http://www.3djuegos.com/"
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:
        html = BeautifulSoup(req.text, 'html.parser')
        entradas = html.find_all('div',{'class':'nov_main'})
	
    for i,entrada in enumerate(entradas):
	referencia=entrada.find('a')
	referencia=format(referencia['href'])
        titulo = entrada.find('h3').getText()
        imagen = entrada.find('img')
        imagen = format(imagen['data-src'])
        mensaje[i]=({'titulo': titulo.encode("utf-8"), 'imagen':imagen,'referencia':referencia})
    return mensaje


def extraerContenido(url):  
    mensaje = {}  
    req = requests.get(url)
    statusCode = req.status_code

    if statusCode == 200:
        html = BeautifulSoup(req.text, 'html.parser')
	video = html.find('meta',{'itemprop':'contentURL'})
        entradas = html.find_all('p',{'class':'s16 fftext c2 lh27 img100 a_n mar_rl2'})
    if video!=None:
    	video=format(video['content'])
    texto_final=""
    for i,entrada in enumerate(entradas):
        texto = entrada.getText()
	texto_final+=texto
    mensaje=({'texto': texto_final.encode("utf-8"),'video':video})
    return mensaje
