n = int(input("Enter the number of participents : "))
k = int(input("Enter the cut off position : "))
if((k<1 or k>n) or (n<k or n>50)):
   print("invalid input")
else:
   s=[]
   c=0
   m=0
   print("Enter the points in decreasing order : ")
   for i in range(n):
       s.append(int(input()))

   for i in range(n):
       if(s[i]==0):
           m += 1
           if(m==k):
               break
       elif(s[i]>=s[k]):
           c += 1
       elif(s[i]<s[k]):
           c += 0
print(c)
