def f(x):
    f=(x**4)-(7*(x**3))+(13*(x**2))+(23*x)-78
    return f
    (x**4)-(6*(x**3))+(11*(x**2))-(17*x)+17 

a=3.0001
b= 5.05005
e=0.01
f1=f(a)
f2=f(b) 
d=0 
central=(a+b)/2
sum=0

while sum==0:
    d=d+1
    if f(central)<0:
        a=central
        central=(a+b)/2
    elif f(central)>0 and f(central)<e:
        sum=sum+1
    else:
        b=central
        central=(a+b)/2
def r():
    print(central)
    print(d)
    return

0.001,4.5
3.0001, 5.05005
-5,-1.5000501

-5.8, 2.0006
2.006, 7.6508
4.082 , 8.35