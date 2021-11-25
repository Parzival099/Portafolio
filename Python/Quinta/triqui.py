import random
archivo = open("intro.txt", mode="r", encoding="utf-8")
himno = archivo.read()
print(himno)
archivo.close()
pass

lista=[" "," "," "," "," "," "," "," "," "," "]
def drawBoard(lista):
    print(lista[7],"|",lista[8],"|",lista[9])
    print("---------------")
    print(lista[4],"|",lista[5],"|",lista[6])
    print("---------------")
    print(lista[1],"|",lista[2],"|",lista[3])
    return(" ")
pass

x=input("Escoja entre X o O")
while x != "X" and x != "O":
        x=input("Escoja entre X o O")
if x=="X":
    y="O"
else:
    y="X"

list = ["Usuario","Computadora"]
def whoGoesFirst():
    if random.choice(list)=="Usuario":
        return("Usuario")
    else:
        return("Computadora")

pass

def makeMove(lista):
    w=int(input("En  que posicion desea poner su significador"))
    return(w)

pass

def isWinner(lista, x):
    if lista[1]==x and  lista[2]==x and lista[3]==x:
         return(True)
    elif lista[4]==x and  lista[5]==x and lista[6]==x:
         return(True)
    elif lista[7]==x and  lista[8]==x and lista[9]==x:
         return(True)
    elif lista[1]==x and  lista[4]==x and lista[7]==x:
         return(True)
    elif lista[2]==x and lista[5]==x and lista[8]==x:
         return(True)
    elif lista[3]==x and lista[6]==x and lista[9]==x:
         return(True)
    elif lista[1]==x and lista[5]==x and lista[9]==x:
         return(True)
    elif lista[3]==x and lista[5]==x and lista[7]==x:
        return(True)
    else:
         return(False)
pass

def isWinner2(lista, y):
    if lista[1]==y and  lista[2]==y and lista[3]==y:
         return(True)
    elif lista[4]==y and  lista[5]==y and lista[6]==y:
         return(True)
    elif lista[7]==y and  lista[8]==y and lista[9]==y:
         return(True)
    elif lista[1]==y and  lista[4]==y and lista[7]==y:
         return(True)
    elif lista[2]==y and lista[5]==y and lista[8]==y:
         return(True)
    elif lista[3]==y and lista[6]==y and lista[9]==y:
         return(True)
    elif lista[1]==y and lista[5]==y and lista[9]==y:
         return(True)
    elif lista[3]==y and lista[5]==y and lista[7]==y:
        return(True)
    else:
         return(False)
pass


def isSpaceFree(lista):
    w=int(input("Que casilla desea verificar"))
    if lista[w]==" ":
        return(True)
    else:
        return(False)
pass
    
def getPlayerMove(lista, x):
    y=int(input("Que casilla desea marcar"))
    while lista[y]!=" ":
        y=int(input("Que casilla desea marcar"))
    lista[y] = x
    return(lista)
pass
        
def chooseRandomMoveFromList(lista):
    w=1
    if w<=10:
        for i in lista:
            if i==" ":
                return(w)
                w=w+1
            else:
                w=w+1
    else:
        if w==0:
            return(" ")
        else:
            return(None)

pass

def getComputerMove(lista):
    if lista[3]==y and lista[1]==y and lista[2]==" ":
        lista[2]=y
        return(lista)
    elif lista[2]==y and lista[3]==y and lista[1]==" ":
        lista[1]=y
        return(lista)
    elif lista[1]==y and lista[2]==y and lista[3]==" ":
        lista[3]==y
        return(lista)
    elif lista[4]==y and lista[5]==y and lista[6]==" ":
        lista[6]=y
        return(lista)
    elif lista[4]==y and lista[6]==y and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[5]==y and lista[6]==y and lista[4]==" ":
        lista[4]=y
        return(lista)
    elif lista[7]==y and lista[8]==y and lista[9]==" ":
        lista[9]=y
        return(lista)
    elif lista[8]==y and lista[9]==y and lista[7]==" ":
        lista[7]=y
        return(lista)
    elif lista[7]==y and lista[9]==y and lista[8]==" ":
        lista[8]=y
        return(lista)
    elif lista[1]==y and lista[9]==y and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[1]==y and lista[5]==y and lista[9]==" ":
        lista[9]=y
        return(lista)
    elif lista[9]==y and lista[5]==y and lista[1]==" ":
        lista[1]=y
        return(lista)
    elif lista[3]==y and lista[7]==y and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[3]==y and lista[5]==y and lista[7]==" ":
        lista[7]=y
        return(lista)
    elif lista[7]==y and lista[5]==y and lista[3]==" ":
        lista[3]=y
        return(lista)
    elif lista[1]==y and lista[7]==y and lista[4]==" ":
        lista[4]=y
        return(lista)
    elif lista[1]==y and lista[4]==y and lista[7]==" ":
        lista[7]=y
        return(lista)
    elif lista[7]==y and lista[4]==y and lista[1]==" ":
        lista[1]=y
        return(lista)
    elif lista[2]==y and lista[5]==y and lista[8]==" ":
        lista[8]=y
        return(lista)
    elif lista[2]==y and lista[8]==y and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[8]==y and lista[5]==y and lista[2]==" ":
        lista[2]=y
        return(lista)
    elif lista[3]==y and lista[6]==y and lista[9]==" ":
        lista[9]=y
        return(lista)
    elif lista[3]==y and lista[9]==y and lista[6]==" ":
        lista[6]=y
        return(lista)
    elif lista[6]==y and lista[9]==y and lista[3]==" ":
        lista[3]=y
        return(lista)
    #2
    if lista[3]==x and lista[1]==x and lista[2]==" ":
        lista[2]=y
        return(lista)
    elif lista[2]==x and lista[3]==x and lista[1]==" ":
        lista[1]=y
        return(lista)
    elif lista[1]==x and lista[2]==x and lista[3]==" ":
        lista[3]==y
        return(lista)
    elif lista[4]==x and lista[5]==x and lista[6]==" ":
        lista[6]=y
        return(lista)
    elif lista[4]==x and lista[6]==x and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[5]==x and lista[6]==x and lista[4]==" ":
        lista[4]=y
        return(lista)
    elif lista[7]==x and lista[8]==x and lista[9]==" ":
        lista[9]=y
        return(lista)
    elif lista[8]==x and lista[9]==x and lista[7]==" ":
        lista[7]=y
        return(lista)
    elif lista[7]==x and lista[9]==x and lista[8]==" ":
        lista[8]=y
        return(lista)
    elif lista[1]==x and lista[9]==x and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[1]==x and lista[5]==x and lista[9]==" ":
        lista[9]=y
        return(lista)
    elif lista[9]==x and lista[5]==x and lista[1]==" ":
        lista[1]=y
        return(lista)
    elif lista[3]==x and lista[7]==x and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[3]==x and lista[5]==x and lista[7]==" ":
        lista[7]=y
        return(lista)
    elif lista[7]==x and lista[5]==x and lista[3]==" ":
        lista[3]=y
        return(lista)
    elif lista[1]==x and lista[7]==x and lista[4]==" ":
        lista[4]=y
        return(lista)
    elif lista[1]==x and lista[4]==x and lista[7]==" ":
        lista[7]=y
        return(lista)
    elif lista[7]==x and lista[4]==x and lista[1]==" ":
        lista[1]=y
        return(lista)
    elif lista[2]==x and lista[5]==x and lista[8]==" ":
        lista[8]=y
        return(lista)
    elif lista[2]==x and lista[8]==x and lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[8]==x and lista[5]==x and lista[2]==" ":
        lista[2]=y
        return(lista)
    elif lista[3]==x and lista[6]==x and lista[9]==" ":
        lista[9]=y
        return(lista)
    elif lista[3]==x and lista[9]==x and lista[6]==" ":
        lista[6]=y
        return(lista)
    elif lista[6]==x and lista[9]==x and lista[3]==" ":
        lista[3]=y
        return(lista)
    elif lista[1]==" ":
        lista[1]=y
        return(lista)
    elif lista[3]==" ":
        lista[3]=y
        return(lista)
    elif lista[7]==" ":
        lista[7]=y
        return(lista)
    elif lista[9]==" ":
        lista[9]=y
        return(lista)
    elif lista[5]==" ":
        lista[5]=y
        return(lista)
    elif lista[2]==" ":
        lista[2]=y
        return(lista)
    elif lista[4]==" ":
        lista[4]=y
        return(lista)
    elif lista[6]==" ":
        lista[6]=y
        return(lista)
    elif lista[8]==" ":
        lista[8]=y
        return(lista)
    else:
        print(" ")
pass




def isBoardFull(lista):
        if lista[1]!=" " and lista[2]!=" " and lista[3]!=" " and lista[4]!=" " and lista[5]!=" " and lista[6]!=" " and lista[7]!=" " and lista[8]!=" " and lista[9]!=" ":
                return(True)
        else:
            return(False)
            
pass

    