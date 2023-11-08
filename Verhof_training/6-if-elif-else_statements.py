#this program tells you if an input value is negative, zero, one or greater than one
x = int(input("please enter an integer"))

if x < 0:
    print ("negative")
elif x == 0:
    print ("zero")
elif x == 1:
    print ("one")
else:
    print ("greater than one")
    