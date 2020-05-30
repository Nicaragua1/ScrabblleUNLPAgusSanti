import funciones
import PySimpleGUI as sg
import colocarFichas as colocar
import random 

sg.theme_background_color(color='Lavender')
sg.theme_button_color(color=('Lavender', 'Lavender'))
sg.theme_element_background_color(color='Lavender')


def randomLetra(bolsa):
    otro = True
    while(otro):
        letra = random.choice(list(bolsa))
        if(bolsa[letra]['cant'] > 0):
            otro = False
            bolsa[letra]['cant'] = bolsa[letra]['cant']-1
    return letra


def repartir(letras, bolsa, window, colores):
	for x in letras:
		if(letras[x]=='' or letras[x] in colores):
			letra=randomLetra(bolsa)
			if(x.find('u')!=-1):
				window[x].update(image_filename=letra)
			letras[x]=letra

def intercambiarFichas(letras, bolsa, window, cant):
	if(cant==7):
		for x in letras:
			letra=randomLetra(bolsa)
			window[x].update(image_filename=letra)
			bolsa[letras[x]]['cant']=bolsa[letras[x]]['cant']+1
			letras[x]=letra
	else:
		cambios=list()
		for _ in range(cant):
			sigo=True
			while(sigo):
				event,_=window.read()
				if not event in cambios:
					cambios.append(event)
					sigo=False
			letra=randomLetra(bolsa)
			window[event].update(image_filename=letra)
			letras[event]=letra
			bolsa[letras[event]]['cant']=bolsa[letras[event]]['cant']+1
	sg.popup('Intercambio realizado!')


puntajeM='0'
puntajeU='0'
tableroIm=dict()
vacios= ['vacio.png','vacio1.png','vacio2.png','vacio3.png','vacio4.png','vacio5.png','vacio6.png','vacio7.png']
tablero = []      ########GENERA TABLERO#######
for x in range(10):
	row = []
	for y in range(10):
		im=random.choice(vacios)
		tableroIm[(x,y)]=im
		row.append(sg.RButton('',image_filename=im,border_width=0,image_size=(50, 50),size=(50,50),pad=(0,0),key=(x,y))) ##el filename no funciona
	tablero.append(row)
tableroFichas=dict()
bolsa={'A.png':{'cant':11,'valor':1}, 'B.png':{'cant':11,'valor':3}, 'C.png':{'cant':8,'valor':1},'D.png':{'cant':7,'valor':1}, 'E.png':{'cant':7,'valor':1}, 'F.png':{'cant':7,'valor':1}, 'G.png':{'cant':7,'valor':1}, 'H.png':{'cant':5,'valor':1}, 'I.png':{'cant':7,'valor':1}, 'J.png':{'cant':7,'valor':1}, 'K.png':{'cant':7,'valor':1}, 'L.png':{'cant':7,'valor':1},'M.png':{'cant':7,'valor':1},'N.png':{'cant':7,'valor':1},'Ñ.png':{'cant':7,'valor':1},'O.png':{'cant':7,'valor':1},'P.png':{'cant':7,'valor':1},'Q.png':{'cant':7,'valor':1},'R.png':{'cant':7,'valor':1},'S.png':{'cant':7,'valor':1},'T.png':{'cant':7,'valor':1},'U.png':{'cant':7,'valor':1},'V.png':{'cant':7,'valor':1},'W.png':{'cant':7,'valor':1},'X.png':{'cant':7,'valor':1},'Y.png':{'cant':7,'valor':1},'Z.png':{'cant':7,'valor':1},'LL.png':{'cant':7,'valor':1},'RR.png':{'cant':7,'valor':1}}
letrasU={'u0':'', 'u1':'','u2':'','u3':'','u4':'','u5':'','u6':''}
letrasM={'m0':'', 'm1':'','m2':'','m3':'','m4':'','m5':'','m6':''}
column1=[
		[sg.Button('Exit',font=('Fixedsys'), size=(20,3))], 
		[sg.Button('palabra',font=('Fixedsys'))],
		[sg.Image('bolsachica.png')],
		[sg.Button('',image_filename='intercambiar.png',border_width=0,font=('Fixedsys'), key='intercambiar')]
		]
layout =[
		[sg.Text('Puntaje: '),sg.Text(puntajeM)],
		[sg.Image('robot.png'),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='m0',size=(50,50)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='m1', size=(4,2)),sg.Button('',image_filename='color3.png',image_size=(50, 50),key='m2', size=(4,2)),sg.Button('',image_filename='color4.png',image_size=(50, 50),key='m3', size=(4,2)),sg.Button('',image_filename='color5.png',image_size=(50, 50),key='m4', size=(4,2)),sg.Button('',image_filename='color1.png',image_size=(50, 50),key='m5',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='m6', size=(4,2)),sg.Text(' ', background_color='Lavender'),sg.Button('',image_filename='comenzar.png',border_width=0,font=('Fixedsys',18), key='comenzar')],
		[sg.Column(tablero),sg.Column(column1)], ##tablero aca
		[sg.Image('jugador.png'),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='u0',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50),key='u1', size=(4,2)),sg.Button('',image_filename='color3.png',image_size=(50, 50), key='u2', size=(4,2)),sg.Button('',image_filename='color4.png',image_size=(50, 50), key='u3', size=(4,2)),sg.Button('',image_filename='color5.png',image_size=(50, 50), key='u4', size=(4,2)),sg.Button('',image_filename='color1.png',image_size=(50, 50), key='u5',size=(4,2)),sg.Button('',image_filename='color2.png',image_size=(50, 50), key='u6', size=(4,2))],
		[sg.Text('Puntaje: '),sg.Text(puntajeU)]
		]
intercambiar=[
			[sg.Text('Cant de fichas a intercambiar')],
			[sg.Spin([i for i in range(1,8)], initial_value=1,key='cant')],
			[sg.Button('Aceptar')]
			]

colores= ['color1.png','color2.png','color3.png','color4.png','color5.png']

window = sg.Window('tablero', layout)
popinter = sg.Window('intercambio', intercambiar)
event, values = window.read()
primer=True
if(event=='comenzar'):
	repartir(letrasU, bolsa, window, colores)
	repartir(letrasM, bolsa, window, colores)
	hide = False
	while True:
		primer, event=colocar.colocarFicha(tableroIm,tableroFichas,letrasU, window,colores, primer)
		if(event=='palabra'):
			repartir(letrasU, bolsa, window, colores)
		if(event=='intercambiar'):
			if(hide):
				popinter.UnHide()
			event, values= popinter.read()
			popinter.Hide()
			hide=True
			intercambiarFichas(letrasU, bolsa, window, values['cant'])
		if event in (None, 'Exit'):
			break 	
window.close()
