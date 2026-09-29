"""
# task1 
from math import pi 

if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    print("Area of the circle with radius", r, "is:", str(pi*r*2))

"""


"""
#task2

# Simple varivable declaration and output 
zahl = 10
print ("The value of zahl:",zahl, "and type is : " , type(zahl))

kommazhal = 10.5 
print ("\nThe value of kommazhal:",kommazhal, "and type is : " , type(kommazhal)) 

text = '"Hello World"'
print ("\nThe value of text:",text, "and type is : " , type(text))

wahrheitwert = True
print ("\nThe value of wahrheitwert:",wahrheitwert, "and type is : " , type(wahrheitwert))

"""


#task 3


"""

if __name__ == "__main__":

    # int -> float 
    x = int(input("Enter an integer: "))
    print("Integer value: ", x, "and type is: ", type(float(x)))

    # int -> str 
    x = int(input("Enter an integer: "))
    print("Integer value: ", x, "and type is: ", type(str(x)))

    # int -> bool
    x = int(input("Enter an integer: "))
    print("Integer value: ", x, "and type is: ", type(bool(x)))

    # float -> int 
    x = float(input("Enter a float: "))
    print("Float value: ", x, "and type is: ", type(int(x)))

    # string -> int
    x = (input("Enter a string: "))
    print("String value: ", x, "and type is: ", type((x)))

"""



#task 4
# Create a program which will calculate the factorial (n! 펙토리얼)

"""
if __name__ == "__main__":
    x = int(input("Enter a number to calculate its factorial: "))
    factorial = 1 
    for i in range(1, x+1 ):
        factorial *= i
    print("Resut: ", factorial)

"""