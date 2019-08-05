a = []
n=int(input("Enter the number of candles : "))

c = 0
print("Enter the size of them : ")
for i in range(n):
    m = []
    m.append(int(input()))
    a.append(m)
    
g = max(a)

for i in range(n):
    if(a[i]==g):
        c += 1

print("The number of tallest candles are : ",c)

