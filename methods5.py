import math
from sympy import *
import numpy as np
x = Symbol('x')

def Newton_Raphson():
    f = eval(input("enter your function here>>\n"))
    f_prime = diff(f,x)
    a = float (input ("enter the value of xi"))
    for i in range (6):
        print("_________________________\n")
        print ("no. of iterations =" , i)
        print ("xi = " ,a)
        print("f(x)= \n" ,f.subs(x,a))
        print("f'(x) = \n" ,f_prime.subs(x,a))
        a = a - (f.subs(x,a)/f_prime.subs(x,a))
        print("xi+1 = \n", a)



def Secant():
    f = eval(input("enter your function here>>\n"))
    f_prime = f.diff(x)
    a = float (input ("enter the value of xi-1 \t"))
    b = float (input ("enter the value of xi \t"))
    for i in range (6):
        print("_________________________\n")
        print ("no. of iterations =" , i)
        print ("xi-1 = \t " ,a)
        print("f(xi-1)= \n" ,f.evalf(subs= {x:a}))
        print ("xi = \t " ,b)
        print("f(xi) = \n" ,f.evalf(subs= {x:b}))
        n = float (b - (f.evalf(subs= {x:b})* ((b-a)/(f.evalf(subs= {x:b})-f.evalf(subs= {x:a})))))
        a=b
        b=n
        print("xi+1 = \n", n)

def Flase_position():
    f = eval(input("enter your function here>>\n"))
    f_prime = f.diff(x)
    a = float (input ("enter the value of xi-1 \t"))
    b = float (input ("enter the value of xi \t"))
    r = int(input("enter the no. of iterations"))
    for i in range (r):
        print("_________________________\n")
        print ("no. of iterations =" , i)
        print ("xi-1 = \t " ,a)
        print("f(xi-1)= \n" ,f.subs(x,a))
        print ("xi = \t " ,b)
        print("f(xi) = \n" ,f.subs(x,b))
        n = float (a - (f.subs(x,a)* ((b-a)/((f.subs(x,b))-f.subs(x,a)))))
        print ("rel. error",abs(b-n))
        a=b
        b=n
        print("xi+1 = \n", n)

def Muller():
    f = eval(input("enter your function here>>\n"))
    a = float (input ("enter the value of x0 \t"))
    b = float (input ("enter the value of x1 \t"))
    c = float (input ("enter the value of x2 \t"))
    r = int(input("enter the number of iterations \t"))
    for i in range (r):
        print("_________________________\n")
        print ("no. of iterations =" , i+1)
        h0 = b-a
        h1 = c-b
        gamma0 = (f.evalf(subs= {x:b})-f.evalf(subs= {x:a}))/(b-a)
        gamma1 = (f.evalf(subs= {x:c})-f.evalf(subs= {x:b}))/(c-b)
        v= (gamma1-gamma0)/(h1+h0)
        j= v*h1+gamma1
        d= f.evalf(subs= {x:c})
        print ("x0 = \t " ,a)
        print("f(x0)= \n" ,f.evalf(subs= {x:a}))
        print ("x1 = \t " ,b)
        print("f(x1) = \n" ,f.evalf(subs= {x:b}))
        print ("x2 = \t " ,c)
        print("f(x2) = \n" ,f.evalf(subs= {x:c}))
        print("h0 == \t", h0)
        print("h1== \t",h1)
        print("gamma0== \t", gamma0)
        print("gamma1== \t", gamma1)
        print("a== \t", v)
        print("b== \t", j)
        print("c== \t", d)
        

        n = float (c + ((-2*d)/(j+math.sqrt(j**2-4*v*d))))
        a=b
        b=c
        c=n
        h0=h1
        gamma0=gamma1
        print("x3 = \t", n)

def Bisection():
    f = eval(input("enter your function here>>\n"))
    a = float (input ("enter the value of a>> \t"))
    b = float (input ("enter the value of b>> \t"))
    sigma = float (input ("enter the value of sigma>> \t"))
    c= (a+b)/2
    i=1
    n =(math.log(b-a)- math.log(sigma))/math.log(2)
    while(f.evalf(subs= {x:c})!=0 or i+1!=n or (b-a)>sigma ):
        print("____________________\n")
        print("a=",a)
        print("b=",b)
        print("f(a) = \n" ,f.evalf(subs= {x:a}))
        print("f(b) = \n" ,f.evalf(subs= {x:b}))
        c= (a+b)/2
        print("c=",c)
        print("f(c) = \n" ,f.evalf(subs= {x:c}))
        if ((f.evalf(subs= {x:a})*f.evalf(subs= {x:c})) <0):
            b=c
        else:
            a=c
        i=i+1
        if (f.evalf(subs= {x:c})==0):
            break
        elif (i+1==n):
            break
        elif ((b-a)<sigma):
            break 

def proterm(i, value, x):  
    pro = 1;  
    for j in range(i):  
        pro = pro * (value - x[j]);  
    return pro;  
  
def dividedDiffTable(x, y, n): 
  
    for i in range(1, n):  
        for j in range(n - i):  
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j])); 
    return y; 
  
def applyFormula(value, x, y, n):  
  
    sum = y[0][0];  
  
    for i in range(1, n): 
        sum = sum + (proterm(i, value, x) * y[0][i]);  
      
    return sum;  
  

def printDiffTable(y, n):  
  
    for i in range(n):  
        for j in range(n - i):  
            print(round(y[i][j], 4), "\t",  
                               end = " ");  
  
        print("");  

def newton_int ():
    n =int(input("enter the no. of columns>> \t"))
    x = np.zeros((n))
    y = [[0 for i in range(10)]  
            for j in range(10)]  
    for i in range(n):
          x[i] = float(input( 'x['+str(i)+']='))
          y[i][0] = float(input( 'y['+str(i)+']='))
    y=dividedDiffTable(x, y, n)  
    printDiffTable(y, n)  
    value = float(input("enter the value of x>> \t"))  
    print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 2))
    
def Lagrange ():
    n = int(input('Enter the no. of columns \n'))
    x = np.zeros((n))
    y = np.zeros((n))
    print('Enter data for x and y >> \n')
    for i in range(n):
        x[i] = float(input( 'x['+str(i)+']='))
        y[i] = float(input( 'y['+str(i)+']='))
    xp = float(input('Enter the value of x >> \t '))
    yp = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (xp - x[j])/(x[i] - x[j])
        yp = yp + p * y[i]
        l= p*y[i]
        print('l(%d)=%f\t'% (i,l))    
    print('Interpolated value at %.3f is %.4f.' % (xp, yp))


def Euler():
    y = Symbol ('y')
    f = eval(input("enter your function here>>\n"))
    n = int(input("enter no. of steps>> \t"))
    h = float (input("enter the width(h)>> \t"))
    x1 = float(input("enter x initial \t"))
    y1 = float(input("enter y initial \t"))
    for i in range ((n)):
        print("_____________________\n")
        print("Step %d "% (n-1))
        x2 = x1+h
        y2 = y1 + h*f.subs([(x,x1),(y,y1)]) 
        print("x2 =\t ",x2)
        print("y2 =\t ",y2)
        x1 = x2
        y1 = y2
        n=n+1

def RK4():
    y = Symbol ('y')
    f = eval(input("enter your function here>>\n"))
    n = int(input("enter no. of steps>> \t"))
    h = float (input("enter the width(h)>> \t"))
    x1 = float(input("enter x initial \t"))
    y1 = float(input("enter y initial \t"))
    for i in range ((n)):
        print("_____________________\n")
        print("Step %d "% (n-1))
        k1 = f.subs([(x,x1),(y,y1)])
        k2 = f.subs([(x,(x1+h/2)),(y,(y1+(h/2)*k1))])
        k3 = f.subs([(x,(x1+h/2)),(y,(y1+(h/2)*k2))])
        k4 = f.subs([(x,(x1+h)),(y,(y1+(k3*h)))])
        x2 = x1+h
        y2 = y1 + (h/6)*(k1+2*k2+2*k3+k4) 
        print("K1 = \t ",k1)
        print("K2 = \t ",k2)
        print("K3 = \t ",k3)
        print("K4 = \t ",k4)
        print("x2 =\t ",x2)
        print("y2 =\t ",y2)
        x1 = x2
        y1 = y2
        n=n+1

def adam():
    y = Symbol ('y')
    f = eval(input("enter your function here>>\n"))
    n = int(input("enter no. of steps>> \t"))
    h = float (input("enter the width(h)>> \t"))
    x1 = float(input("enter x initial \t"))
    y1 = float(input("enter y initial \t"))
    k1 = f.subs([(x,x1),(y,y1)]) 
    k2 = f.subs([(x,(x1+h)),(y,(y1+k1*h))])
    x2 = x1 +h
    y2 = y1 +((h/2)*(k1+k2))
    print("Using RK2>>>\n")
    print("x1= \t",x1)
    print("y1= \t",y1)
    print("k1= \t",k1)
    print("k2= \t",k2)
    print("x2= \t",x2)
    print("y2= \t",y2)
    for i in range(n):
        print("_____________________\n")
        print("Step %d "% (n-1))
        x3 = x2 +h
        y3= y2+h*((3/2)*f.subs([(x,x2),(y,y2)])-(1/2)*f.subs([(x,x1),(y,y1)]))
        print("y2 = \t",y3)
        x1=x2
        y1=y2
        x2=x3
        y2=y3





        
print("__Welcome to Numerical Solver__ \n")

i= input("Please Choose The Method You Want >>>\n a)Bisection\n b)Newton Raphson\n c)Secant\n d)False Position\n e)Muller\n f)Lagrange\n g)Newton Divided Diff\n h)Euler\n i)RK4 \n j)Adams-Bashforth \n ") 
if (i =='a'):
    Bisection()
elif (i == 'b'):
    Newton_Raphson()   
elif (i == 'c'):
    Secant()
elif (i == 'd'):
    Flase_position()
elif (i == 'e'):
    Muller()
elif (i == 'f'):
    Lagrange()
elif (i== 'g'):
    newton_int()
elif (i== 'h'):
    Euler()
elif (i=='i'):
    RK4()
elif (i=='j'):
    adam()