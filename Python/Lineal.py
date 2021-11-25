d={'a':0,'b':1,'c':2}#lineal
def t():
    L=[-255000, -134531, -1000, -100, -100, -100, -10, -5, -1, 0, 0, 0, 0, 1, 1, 2,2,2, 17, 21, 22, 22, 100,100, 102, 103, 104, 105, 106, 107, 107, 150000 ] 
    q=int(input("Ingrese el numero a buscar"))
    
    ban=False
    n=0
    sum=0
    while ban==False and n<=(len(L)-1) and L[n]!=q:
            if ban==False:
                n=n+1
                sum=sum+1
            elif L[n] == (q):
                print("yes")
                ban==True
                
    return(sum+1)
