#Exhaustiva
def g():
    def f(x):
        f=(x**4)-(6*(x**3))+(11*(x**2))-(17*x)+17
        "(x**4)-(6*(x**3))+(11*(x**2))-(17*x)+17 "
        return f
    
    sum=0
    a=4.082 
    b=8.35
    e=0.01
    xl=a
    
    while xl<=b and xl>=a:
        xl=xl+0.0001
        sum=sum+1
        if f(xl)<e and f(xl)>-e:
            print(xl)
                
                
        else:
            xl=xl+0
    
    print(sum)
    return()
    

0.001,4.5
3.0001, 5.05005
-5,-1.5000501

-5.8, 2.0006
2.006, 7.6508
4.082 , 8.35