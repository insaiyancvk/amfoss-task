n = int(input("Enter the number of words you want to enter : "))
w = []
l = []
e = ''
print("Enter the words : ")
for i in range(0,n):
    w.append(input())

print("The abbriviation : ")
for j in range(n):
    e = w[j]
    l = len(w[j])
    if(l>10):
        print(e[0]+str(l-2)+e[l-1])
    else:
        print(w[j])
    
