x=[]
numbers=1
while (numbers!='q'):
    numbers=input("insert number:")
    x.append(numbers)
x.remove(x[-1])
print("largest number is",max(x))
print("smallest number is",min(x))