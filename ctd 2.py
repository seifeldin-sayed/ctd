def enter_number(bag):
    number=input("Enter a number: ")
    if number.isdigit():
        bag.append(int(number))
    else:
        return(enter_number(bag))
def remove_number(bag):
    number=input("Enter a number: ")
    if number.isdigit():
        if int(number) in bag:
            bag.remove(int(number))
        else:
            print(number + " not in list" )
    else:
        return(remove_number(bag))
bag=[6,22,10,999,76,43]
while True:
    print(bag)
    Type=input("choose enter or remove or sort or stop: ").lower()
    if Type=="enter":
        enter_number(bag)
    elif Type=="remove":
        if len(bag)>5:
            remove_number(bag)
        else:
            print("Cannot remove, bag is at minimum capacity")
    elif Type=="sort":
        bag.sort()
    else:
        break
