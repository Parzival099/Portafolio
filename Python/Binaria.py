#Binaria
def y():
    L=[-255000, -134531, -1000, -100, -100, -100, -10, -5, -1, 0, 0, 0, 0, 1, 1, 2,2,2, 17, 21, 22, 22, 100,100, 102, 103, 104, 105, 106, 107, 107, 150000 ]
    x=int(input("Ingrese el numero a investigar"))
    
    if L.count(x)>=1:
            q=(L.index(x))
            X=0
            Z=len(L)
            ban=False
            sum=0
            central=(X+Z)//2
        
            while ban==False :
                sum=sum+1
                if central==q:
                    sum=sum+1
                    ban=True
                        
                else:
                    if central>q:
                            Z=central
                            central=(X+Z)//2
                    elif central<q:
                            X=central
                            central=(X+Z)//2                   
    return(sum)



    

        
            
            