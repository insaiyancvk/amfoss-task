m = []
d1 = 0
d2 = 0
c = int(input("Enter the size of array : "))

print("Enter the values row wise : ")

for i in range(0,c):
    a = []
    for j in range(0,c):
        a.append(int(input()))
    m.append(a)

for i in range(0,c):
    for j in range(0,c):
        if(i==j):
            d1 += m[i][j]
            
for i in range(0,c):
    for j in range(0,c):
        if(i==c-j-1):
            d2 += m[i][j]

if((d1-d2)>=0):
    print("The difference between the sum of the diagonals of the matrix is : ",(d1-d2))
elif((d1-d2)<0):
    print("The absolute difference between the sum of diagonals of the matrix is : ",(d2-d1))
