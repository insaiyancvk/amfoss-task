a = input("Enter the time in hh:mm:ssAM or hh:mm:ssPM format : ")

b = len(a)

s = a[b-2]

h1 = 0
h2 = 0
h1 = int(a[0])
h2 = int(a[1])

hh = (h1*10)+h2+12


if(hh>24 or ((int(a[3])>5) or ((int(a[6])>5)))):
    print("Invalid input")
else:
    if(s=='A' or s=='a'):
        print(a[0:8])

    elif(s=='P' or s=='p'):
        print((str(hh))+(a[2:8]))
