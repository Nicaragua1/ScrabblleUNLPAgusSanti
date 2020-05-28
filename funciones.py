#"windows" if "win" in sys.platform else "linux"
from pattern.es import *
from pattern.web import Wiktionary
import PySimpleGUI as sg

w = Wiktionary(language="es")

def tipoPalabra(arg):
    analisis = parse(arg).split('/')
    if analisis[1] == "JJ": 
        return "adjetivo"
    elif (analisis[1]) == "VB":
        return "verbo"
    elif (analisis[1] == "NN"):  # No distingue las no palabras de sustantivos, asiq usamos wiktionary en ese caso
        article=w.search(arg)
        if article!=None:
            return "sustantivo"
        else:
            return "no_existe"


def generarTablero():
    tablero = []      
    for x in range(10):
        row = []
        for y in range(10):
            row.append(sg.RButton('',image_filename='images.png',size=(1,1),pad=(0,0),key= (x,y))) ##el filename no funciona
        tablero.append(row)