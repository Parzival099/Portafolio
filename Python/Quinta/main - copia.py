import random
import triqui as tr

lista=[" "," "," "," "," "," "," "," "," "," "]
p=[" "," "," "," "," "," "," "," "," "," "]
x=input("Escoja entre X o O")
if x=="X":
    y="O"
else:
    y="X"
    
list = ["Usuario","Computadora"]
rayo=0
if random.choice(list)=="Usuario":
        rayo="Usuario"
        print("9")
else:
        rayo="Computadora"
        print("8")

    
from triqui import drawBoard
print(drawBoard(lista))

from triqui import isWinner
from triqui import isWinner2

from triqui import getPlayerMove

from triqui import isBoardFull

from triqui import getComputerMove

ban=True
while ban==True:
    if rayo=="Usuario":
        rayo="Computadora"
        print(drawBoard(getPlayerMove(lista,x)))
        if isWinner(lista,x)==True:
            print("Buena partida-El ganador es el jugador")
            ban=False
        if isBoardFull(lista)==True:
            print("Empate")
            ban=False
        while ban==False:
            l=str(input("Desea volver a jugar Y/N"))
            if l=="Y":
                ban==True
                lista=[" "," "," "," "," "," "," "," "," "," "]
            else:
                ban==False
                break
        
    else:
        rayo="Usuario"
        print(drawBoard(getComputerMove(lista)))
        if isWinner2(lista,y)==True:
            print("Buena partida-El ganador es el computador")
            ban=False
        if isBoardFull(lista)==True:
            print("Empate")
            ban=False
        while ban==False:
            l=str(input("Desea volver a jugar y/n"))
            if l=="Y":
                ban==True
                lista=[" "," "," "," "," "," "," "," "," "," "]
            else:
                ban==False
                break
            
        
        
        
        
