# ScrabblleUNLPAgusSanti
![](https://i.imgur.com/O7vRM8o.png)


## Requisitos

Python 3.6.8

PySimpleGUI (Libreria)

Pattern (Libreria)

## Instrucciones

Se debe ejecutar el archivo SrabbleAR.py dentro del directorio scrabble para comenzar el juego. 

Para comenzar la partida se debe tocar 'iniciar'. Todavia no se configuró el funcionamiento de la IA, por lo que siempre es el turno del usuario, y el tiempo no se tiene en cuenta.

La primera ficha debe ser colocada en el centro del tablero.

Al colocar las fichas en el tablero estas se pueden quitar individualmente tocando sobre la ultima colocada, en caso de querer sacar todas se usa el botón 'sacar todas' como antes dicho. En el caso de tener una ficha en mano y arrepentirse de colocarla en el tablero, si se presiona la posición de la ficha en donde estaba en el átril, esta vuelve a donde estaba. 

## Notas adicionales

El archivo funciones.py contiene funciones varias relacionadas al analisis de la palabra formada y su puntaje. El archivo funcionesFichas.py tiene funciones relacionadas al manejo de las fichas como colocarFicha, SacarFicha, Repartir, entre otras. El archivo tableros.py tine los tableros disponibles y una funcion para crear el tablero.
Actualmente se usa un tablero de 15x15 pero uno de 15x20 tambien esta disponible, se tiene que modificar el código del archivo SrabbleAR.py para hacerlo, ya que todavia no se puede configurar desde la interfaz.

## Participantes

Maria Agustina Gonzalez y Santiago Jose Lizondo Colomes.

