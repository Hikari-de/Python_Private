import random
secret = random.randint(1, 20)
lim = 5
while(lim):
    turn_num = int(input("Enter valid value from 1 -> 20: "))
    if(turn_num == secret):
        print("Successful!")
        break
    elif(turn_num < secret):
        print("Lower")
    else:
        print("Upper")
    lim -= 1
