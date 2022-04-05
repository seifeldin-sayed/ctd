import random
def play(bag1,bag2,bag3):
    user=input("Enter bag number: ")
    if user=='1':
        if bag1==1:
            play(bag1,bag2,bag3)
        else:
            ball_number= input("Enter the number of balls from 1 to 5: ")
            bag1=take_value(bag1,ball_number)
    elif user=='2':
        if bag2==1:
            play(bag1,bag2,bag3)
        else:
            ball_number= input("Enter the number of balls from 1 to 5: ")
            bag2=take_value(bag2,ball_number)
    elif user=='3':
        if bag3==1:
            play(bag1,bag2,bag3)
        else:
            ball_number= input("Enter the number of balls from 1 to 5: ")
            bag3=take_value(bag3,ball_number)
    else:
        play(bag1,bag2,bag3)
    return bag1, bag2, bag3
def computer(bag1,bag2,bag3):
    bag=None
    bags=['1','2','3']
    bag=random.choice(bags)
    if (bag=='1' and bag1!=1) or (bag3==1 and bag2==1):
        if bag1<=6:
            ball_number=bag1-1
        else:
            ball_number= random.randint(1,5)
        bag1=take_value(bag1,ball_number)
    elif (bag=='2' and bag2!=1) or (bag1==1 and bag3==1):
        if bag2<=6:
            ball_number=bag2-1
        else:
            ball_number= random.randint(1,5)
        bag2=take_value(bag2,ball_number)
    elif (bag=='3' and bag3!=1) or (bag1==1 and bag2==1):
        if bag3<=6:
            ball_number=bag3-1
        else:
            ball_number=random.randint(1,5)
        bag3=take_value(bag3,ball_number)
    else:
        computer(bag1,bag2,bag3)
    return bag1, bag2, bag3
def take_value(bag,ball_number):
    while 1:
        try:
            ball_number=int(ball_number)
            bag = bag-ball_number
            if int(ball_number)<1 or bag<1 or int(ball_number)>5 :
                bag=bag+ball_number
                ball_number= input("Enter the number of balls from 1 to 5: ")
            else:
                return bag
        except ValueError:
            ball_number= input("Enter the number of balls from 1 to 5: ")
        except TypeError:
            ball_number= input("Enter the number of balls from 1 to 5: ")
def display(bag1,bag2,bag3):
    print(str(bag1-1) + " ball remain in the bag_1")
    print(str(bag2-1) + " ball remain in the bag_2")
    print(str(bag3-1) + " ball remain in the bag_3")
    print("")
def check_win(bag1,bag2,bag3,c):
    if bag1==bag2==bag3==1:
        c=1
        return c
    else:
        c=0
def game():
    bag1=11
    bag2=11
    bag3=11
    c=0
    while bag1>1 or bag2>1 or bag3>1:
        bag1, bag2, bag3=play(bag1,bag2,bag3)
        display(bag1,bag2,bag3)
        c=check_win(bag1,bag2,bag3,c)
        if c==1:
            print("You won")
            exit()
        bag1, bag2, bag3=computer(bag1,bag2,bag3)
        display(bag1,bag2,bag3)
        c=check_win(bag1,bag2,bag3,c)
        if c==1:
            print("You lose")
            exit()
game()