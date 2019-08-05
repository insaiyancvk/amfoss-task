import math

n=float(input("Enter the length of the Theatre square : "))

m=float(input("Enter the breadth of the Theatre square : "))

a=float(input("Enter length of the flagstone : "))

t = (math.ceil(n/a))*(math.ceil(m/a))

print(t)
