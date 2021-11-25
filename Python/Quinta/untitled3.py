lista=["1","2","3","4","5","6","7","8"," "," "]
print(lista[3:6])
def isBoardFull(lista):
    sum=0
    for i in lista:
        sum=sum+1
        if i==" ":
            return(False)
        else:
            if lista[:]!=" ":
                return(True)
            
pass

print(isBoardFull(lista))


 if ban==False:
        while input("Quiere volver a jugar? y/n")=="Y" or input("Quiere volver a jugar? y/n")=="N":
            ban==True
            break