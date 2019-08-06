a=[]
b=[]
c=0
d=0
for i in range (3):
    n=int(input())
    a.append(n)
    

for j in range (3):
    m=int(input())
    b.append(m)

for i in range (len(a)):
        if((b[i]>100 or b[i]<1) and (a[i]>100 or a[i]<1):
            print("Invalid") 
        else:
           if(a[i]>b[i]):
             c=c+1
           else :
              if(a[i]<b[i]):
                d=d+1

print(c,d)
