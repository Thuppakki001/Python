
import random
x=1
while x > 0 :
    num = int(input("how many times would you like to roll\n"))
    x = num
    while num > 0:
        roll = random.randint(1,6)
        print ("your dice roll is",roll)
        num = num - 1
    
