def mode1(c):
    f=1.8*c +32
    return(f)
def mode2(f):
    c=(5/9)*(f-32)
    return(c)
mode=int(input("mode: "))
temp=int(input("temp: "))
if mode==1:
    f=mode1(temp)
    print("temp in fahrenheit is " +str(f))
else:
    c=mode2(temp)
    print("temp in celsius is " +str(c))
    