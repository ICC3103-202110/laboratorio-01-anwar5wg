# -*- coding: utf-8 -*-

from random import shuffle

cartas = int(input('Con cuantos pares desea jugar?')) 

pretab1 = []
pretab2 = []
pretab3 = []
for i in range(1,cartas + 1,1):
    pretab1.append(i)
    pretab1.append(i)
doble = int(cartas*2)
shuffle(pretab1)
pretab2 = pretab1[: cartas]
pretab3 = pretab1[cartas:doble]
tablero = []    
tablero.append(pretab2)
tablero.append(pretab3)

J1 = 0 #pts
J2 = 0 #pts

preoculto1 = []
preoculto2 = []
for i in range(1,cartas + 1,1):
    preoculto1.append(0)
    preoculto2.append(0)
oculto = []
oculto.append(preoculto1)
oculto.append(preoculto2)
for i in oculto:
    print(i)

x=1
while x != 0: 
    print('Turno Jugador 1')     
    a = int(input('Fila?'))-1
    j = int(input('Columna?'))-1
    
    if oculto[a][j] == 0:
        oculto[a][j] = tablero[a][j]
        for i in oculto:
            print(i)
            
    y = int(input('Fila?'))-1
    x = int(input('Columna?'))-1       
    if oculto[y][x] == 0:
        oculto[y][x] = tablero[y][x]
        for i in oculto:
            print(i)    
    if oculto[a][j] == oculto[y][x]:
        oculto[a][j] = ' '
        oculto[y][x] = ' '
        for i in oculto:
            print(i)
        print('Jugador 1 sigue jugando')
    if tablero[a][j] != tablero[y][x]:
        oculto[a][j] = 0
        oculto[y][x] = 0
        for i in oculto:
            print(i)    
        print('Turno Jugador 2')
    if oculto[0].count(0) == 0 and oculto[1].count(0) == 0:
        break
    