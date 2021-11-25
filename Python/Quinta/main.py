import random
import triqui as tr

lista=[" "," "," "," "," "," "," "," "," "," "]
x=input("Reescriba la letra escogida")
while x != "X" and x != "O":
        x=input("Reescriba la letra escogida")
if x=="X":
    y="O"
else:
    y="X"

list = ["Usuario","Computadora"]
rayo=0
if random.choice(list)=="Usuario":
        rayo="Usuario"
        print("Empieza el Usuario")
else:
        rayo="Computadora"
        print("Empieza el Computadora")
 
    
from triqui import drawBoard
print(drawBoard(lista))
from triqui import isWinner
from triqui import isWinner2
from triqui import getPlayerMove
from triqui import isBoardFull
from triqui import getComputerMove


hito=0
jorge=0
pepe=0
l=input("desea empezar a jugar Y/N")
ban=True
while l=="Y" or l=="y":
    lista=[" "," "," "," "," "," "," "," "," "," "]
    print("----------------------------------")
    print("El Ususario ha ganado " + str(pepe))
    print("El Computador ha ganado " + str(hito))
    print("Han empatado " + str(jorge))
    print("----------------------------------")
    pass
    while ban==True:
        if rayo=="Usuario":
            rayo="Computadora"
            print(drawBoard(getPlayerMove(lista,x)))
            if isWinner(lista,x)==True:
                print("Buena partida-El ganador es el jugador")
                ban=False
                pepe=pepe+1
            if isBoardFull(lista)==True:
                print("Empate")
                ban=False
                jorge=jorge+1
            if ban==False:
                l=input("Desea volver a jugar Y/N")
                if l=="Y" or l=="y":
                    ban=True
                    lista=[" "," "," "," "," "," "," "," "," "," "]
                    if random.choice(list)=="Usuario":
                        rayo="Usuario"
                        print("Usuario")
                        l="Y"
                        break
                    else:
                            rayo="Computadora"
                            print("Computadora")
                            l="Y"
                            break
                else:
                    ban=False
                    print("----------------------------------")
                    print("El Ususario ha ganado " + str(pepe))
                    print("El Computador ha ganado " + str(hito))
                    print("Han empatado " + str(jorge))
                    print("----------------------------------")
                    pass
                    break
            
        else:
            rayo="Usuario"
            print(drawBoard(getComputerMove(lista)))
            if isWinner2(lista,y)==True:
                print("Buena partida-El ganador es el computador")
                ban=False
                hito=hito+1
            if isBoardFull(lista)==True:
                print("Empate")
                ban=False
                jorge=jorge+1
            if ban==False:
                l=input("Desea volver a jugar y/n")
                if l=="Y" or l=="y":
                    ban=True
                    lista=[" "," "," "," "," "," "," "," "," "," "]
                    if random.choice(list)=="Usuario":
                        rayo="Usuario"
                        print("Usuario")
                        l="Y"
                        break
                    else:
                            rayo="Computadora"
                            print("Computadora")
                            l="Y"
                            break
                else:
                    ban=False
                    print("----------------------------------")
                    print("El Ususario ha ganado " + str(pepe))
                    print("El Computador ha ganado " + str(hito))
                    print("Han empatado " + str(jorge))
                    print("----------------------------------")
                    pass
                break
        
        
        
        
