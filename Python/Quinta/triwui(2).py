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
if x=="X":
    y="O"
else:
    y="X"
def inputPlayerLetter(x):
    while x != "X" and x != "O":
        x=input("Escoja entre X o O")
    return("A escogido " + x)
print(inputPlayerLetter(x))
pass

list = ["Usuario", "Computadora"]
def whoGoesFirst():
    if random.choice(list)=="Usuario":
        print("Empieza - Usuario")
    else:
        print("Empieza - Computadora")
    return(" ")
print(whoGoesFirst())
pass

def makeMove(lista,x):
    y=int(input("En  que posicion desea poner su significador"))
    lista[y] = x
    print(drawBoard(lista))
    return(" ")
print(makeMove(lista,x))
pass

def isWinner(lista, x):
    if lista[:3] == x or lista[3:6]==x or lista[6:9]==x:
        print("True")
    elif lista[1]== lista[4]== lista[7]:
        print("True")
    elif lista[2]== lista[5]==lista[8]:
        print("True")
    elif lista[3]==lista[6]==lista[9]:
        print("True")
    elif lista[1]==lista[5]==lista[9]:
        print("True")
    elif lista[3]==lista[5]==lista[7]:
       print("True")
    else:
        print("False")
    return(" ")
print(isWinner(lista, x))
pass

w=int(input("Que casilla desea verificar"))
def isSpaceFree(lista, w):
    if lista[w]=="":
        print("True")
    else:
        print("False")
    return(" ")
print(isSpaceFree(lista, w))
pass
    
def getPlayerMove(lista, x):
    y=int(input("Que casilla desea marcar"))
    lista[y] = x
    print("Escogio la casilla " + str(y))
    print(drawBoard(lista))
    return(" ")
print(getPlayerMove(lista,x))
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
print(chooseRandomMoveFromList(lista))
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
        print("Puto")
pass

print(getComputerMove(lista))
print(drawBoard(lista))


def isBoardFull(lista):
    sum=0
    for i in lista:
        sum=sum+1
        if i==" ":
            return(False)
        else:
            if sum==10:
                return(True)
            
print(isBoardFull(lista))
pass

    