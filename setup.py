# -*- coding: utf-8 -*-

from setuptools import setup

#Función de setup requerida por Openshift
setup(name='chachijuegos',
      version='1.0',
      description='Búsqueda de Juegos',
      author='IACA',
      author_email='IACA@alum.uca.es',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Flask==0.10.1', 'beautifulsoup4==4.4.1', 'requests'],
     )
