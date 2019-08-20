import math

n=float(input("Enter the length of the Theatre square : "))

m=float(input("Enter the breadth of the Theatre square : "))

a=float(input("Enter length of the flagstone : "))

t = (math.ceil(n/a))*(math.ceil(m/a))

if((n<1 or n>(math.pow(10,9))) or (m<1 or m>(math.pow(10,9))) or (a<1 or a>(math.pow(10,9)))):
    print("Invalid input") 
else:
    print(t)
