import random
def play(bag1,bag2,bag3):
    user=input("Enter bag number: ")
    while 1:
        if user=='1':
            if bag1==0:
                print("This bag is empty")
            else:
                ball_number= input("Enter the number of balls from 1 to 5: ")
                bag1=take_value(bag1,ball_number)
                break
        elif user=='2':
            if bag2==0:
                print("This bag is empty")
            else:
                ball_number= input("Enter the number of balls from 1 to 5: ")
                bag2=take_value(bag2,ball_number)
                break
        elif user=='3':
            if bag3==0:
                print("This bag is empty")
            else:
                ball_number= input("Enter the number of balls from 1 to 5: ")
                bag3=take_value(bag3,ball_number)
                break
        else:
            print("please choose one of the three bags!!!")
        user=input("Enter a valid bag: ")
    return bag1, bag2, bag3
def computer(bag1,bag2,bag3):
    while 1:
        bag=None
        bags=['1','2','3']
        bag=random.choice(bags)
        if (bag=='1' and bag1!=0) or (bag3==0 and bag2==0):
            if bag1<=5:
                ball_number=bag1
            else:
                ball_number= random.randint(1,5)
            bag1=take_value(bag1,ball_number)
            break
        elif (bag=='2' and bag2!=0) or (bag1==0 and bag3==0):
            if bag2<=6:
                ball_number=bag2
            else:
                ball_number= random.randint(1,5)
            bag2=take_value(bag2,ball_number)
            break
        elif (bag=='3' and bag3!=0) or (bag1==0 and bag2==0):
            if bag3<=5:
                ball_number=bag3
            else:
                ball_number=random.randint(1,5)
            bag3=take_value(bag3,ball_number)
            break
    return bag1, bag2, bag3
def take_value(bag,ball_number):
    while 1:
        try:
            ball_number=int(ball_number)
            bag = bag-ball_number
            if int(ball_number)<1 or int(ball_number)>5 :
                bag=bag+ball_number
                ball_number= input("RE-enter a number from 1 to 5: ")
            elif bag<0:
                bag=bag+ball_number
                print("You have excided the limit of the bag!")
                ball_number= input("RE-enter a number from 1 to the limit: ")
            else:
                break
        except ValueError:
            ball_number= input("RE-enter a number from 1 to 5: ")
        except TypeError:
            ball_number= input("RE-enter a number from 1 to 5: ")
    return bag
def display(bag1,bag2,bag3):
    print(str(bag1) + " ball remain in the bag_1")
    print(str(bag2) + " ball remain in the bag_2")
    print(str(bag3) + " ball remain in the bag_3")
    print("")
def check_win(bag1,bag2,bag3,c):
    if bag1==bag2==bag3==0:
        c=1
        return c
def game(bag1,bag2,bag3,c):
    while bag1>0 or bag2>0 or bag3>0:
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
bag1=bag2=bag3=10
c=0
game(bag1,bag2,bag3,c)
