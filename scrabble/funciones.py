from pattern.text.es import verbs, tag, spelling, lexicon, parse
from sys import platform as _platform
import os
import PySimpleGUI as sg
import json


# esto funciona mandandole un diccionario dentro de la funcion colocar fichas, con un formato asi {(7, 7): 'R.png', (7, 8): 'K.png', (7, 9): 'Z.png'}
def obtener_palabra(d):
    palabraFormada = ''
    for x in d:
        palabraFormada = palabraFormada + (d[x].split('.')[0])
    return(palabraFormada)


def clasificar(cual):
    if cual == "JJ":
        return "adjetivos"
    elif cual == "VB":
        return "verbos"
    else:
        return 'sustantivos'


def tipoPalabra(d):
    palabra = obtener_palabra(d)
    analisis = parse(palabra, tags=True, chunks=False).split(' ')
    tipo = clasificar(analisis)
    #if len(palabra) == 1:      SIRVE PARA TESTEAR POR AHORA
    #    return 'no_existe'
    if(tipo == 'sustantivos'):
        if not palabra.lower() in verbs:
            if not palabra.lower() in spelling:
                if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
                    return 'no_existe'
                else:
                    return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
            else:
                return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
        else:
            return clasificar(tag(palabra, tokenize=True, encoding='utf-8')[0][1])
    else:
        return tipo


def calcularPuntaje(l, im, b):
    suma = 0
    multi = list()
    for x in l:
        cas = im[x]
        if (cas == 'lx2.png'):
            suma = suma+(b[l[x]]['valor']*2)
        elif(cas == 'lx3.png'):
            suma = suma+(b[l[x]]['valor']*3)
        elif(cas == '-1.png'):
            suma = suma+(b[l[x]]['valor']-1)
        elif(cas == '-2.png'):
            suma = suma+(b[l[x]]['valor']-2)
        elif(cas == '-3.png'):
            suma = suma+(b[l[x]]['valor']-3)
        elif(cas == 'px2.png'):
            multi.append(2)
        elif(cas == 'px3.png'):
            multi.append(3)
        else:
            suma = suma+b[l[x]]['valor']
    for y in multi:
        suma = suma*y
    return suma


def barraSistemaoperativo():
    if _platform.startswith == "win":  # windows
        return('/')
    else:  # linux
        return('/')


def carpetaImagenes():
    return os.getcwd() + barraSistemaoperativo() + 'imagenes' + barraSistemaoperativo()


def activarBotones(window):
    window.FindElement("comenzar").Update(visible=False, disabled=True)
    window["comenzar"].Update(visible=False, disabled=True)
    window["intercambiar"].Update(disabled=False)
    window["palabra"].Update(disabled=False)
    window["sacar"].Update(disabled=False)
    window["u0"].Update(disabled=False)
    window["u1"].Update(disabled=False)
    window["u2"].Update(disabled=False)
    window["u3"].Update(disabled=False)
    window["u4"].Update(disabled=False)
    window["u5"].Update(disabled=False)
    window["u6"].Update(disabled=False)
    window.FindElement("intercambiar").Widget.config(cursor="exchange")
    window.FindElement("palabra").Widget.config(cursor="heart")
    window.FindElement("sacar").Widget.config(cursor="pirate")
    window.FindElement("u0").Widget.config(cursor="hand2")
    window.FindElement("u1").Widget.config(cursor="hand2")
    window.FindElement("u2").Widget.config(cursor="hand2")
    window.FindElement("u3").Widget.config(cursor="hand2")
    window.FindElement("u4").Widget.config(cursor="hand2")
    window.FindElement("u5").Widget.config(cursor="hand2")
    window.FindElement("u6").Widget.config(cursor="hand2")


def mostrar_top10(puntajes, configuracion):
    ancho_columnas = (10, 10)
    headings = ("NOMBRE", "PUNTAJE", "DIF", "FECHA")
    columna = [
        [sg.Image(os.path.join('imagenes','rankings.png'))],
    ]
    layout = [
        [sg.Text('TOP PUNTAJES ALTOS', font=('Fixedsys', 20),
                 text_color='salmon', background_color='white'), sg.Image(os.path.join('imagenes','trofeo.png'))],
        [sg.Column(columna, ""), sg.Table(puntajes, headings, select_mode="none", col_widths=ancho_columnas,
                                          num_rows=10, text_color="black", auto_size_columns=True, font=('Fixedsys', 6))],
        [sg.Text('      ', font=('Fixedsys', 18), background_color='white'), sg.Button(
            'VOLVER', font=('Fixedsys', 18), button_color=('orange', 'White'), key='volver')],
    ]
    top10 = sg.Window("TOP 10", layout, resizable=True,
                       finalize=True).Finalize()
    while True:
        event, values = top10.read()
        print(event, values)
        if event == 'volver' or event == None:
            break
    top10.close()
    configuracion.un_hide()


def mostrar_fin_partida():
    try:
        with open("puntajes.json") as arc:
            datos = json.load(arc)
            if not datos:
                sg.popup('Archivo de puntajes no encontrado')
            else:
                puntajes = sorted(datos, reverse=False, key=lambda x: x[1])
                print('pepe')

    except FileNotFoundError:
        sg.popup('Archivo de puntajes no encontrado')


    puntajeU = -1
    puntajeM = 3

    # me fijo si supera al mas bajo de todos para quedar en el top 10
    if puntajeU > puntajes[0][1]:
        quedotop10 = True
    else:
        quedotop10 = False

    # agrego el nuevo puntaje una vez que lo haya escrito y toco el boton OK
    puntajes.append = ["juuuu",  999, "easy", "3/3/2050"]
    print(puntajes)


    print(puntajes[0][1])    

    color_usuario = 'red'
    color_compu = 'red'

    if puntajeU > puntajeM:
        ganador = 'Usuario'
        imagen_ganador = 'jugador.png'
        color_usuario = 'green'
    else:
        ganador = 'Computadora'
        imagen_ganador = 'robot.gif'
        color_compu = 'green'


    layout = [
        [sg.Text('¡La partida ha terminado!', font=('Fixedsys', 30),text_color='salmon', background_color='white')],
        [sg.Text('       Has quedado en el top 10', font=('Fixedsys', 20),text_color='green', background_color='white', visible = quedotop10)],
        [sg.Text('',background_color= 'White')],
        [sg.Text('Ganador: ', font=('Fixedsys', 17),text_color='salmon', background_color='white'), sg.Text(ganador, font=('Fixedsys', 17),text_color='salmon', background_color='white'),sg.Image(os.path.join('imagenes',imagen_ganador))],
        [sg.Text('',background_color= 'White')],
        [sg.Text('Puntuacion Usuario    :', font=('Fixedsys', 17),text_color='salmon', background_color='white'),sg.Text(str(puntajeU), font=('Fixedsys', 20),text_color=color_usuario, background_color='white')],
        [sg.Text('Puntuacion Computadora:', font=('Fixedsys', 17),text_color='salmon', background_color='white'),sg.Text(str(puntajeM), font=('Fixedsys', 20),text_color=color_compu, background_color='white')],
        [sg.Text('',background_color= 'White')],
        [sg.Text('Escribe tu nombre', font=('Fixedsys', 20),text_color='salmon', background_color='white', visible= quedotop10),sg.Input(size=(12,8),font=('Fixedsys', 17),visible= quedotop10),sg.Button('OK', size=(5,2), font=('Fixedsys', 15), button_color=('orange', 'White'), key='volver',visible= quedotop10)],
        [sg.Text('      ', font=('Fixedsys', 45),background_color= 'White'), sg.Button('VOLVER', font=('Fixedsys', 18), button_color=('orange', 'White'), key='volver')],
            ]
    fin_partida = sg.Window("TOP 10", layout, resizable=True,finalize=True).Finalize()
    
    event, values = fin_partida.read()



