n=int(input("Enter the number of increments or decrements :"))

x=0
s=[]
e=''

if(n>=1 and n<=150):
    print("Enter the increment or decrement in format 'x++','++x','x--','--x':")
    for i in range(n):
        s.append(input())
        e=s[i]
        if((e[0:1]=='-' or e[1:2]=='-') and (e[0]=='x' or e[2]=='x' or e[0]=='X' or e[2]=='X')):
            x -= 1
        elif(e[0:1]=='+' or e[1:2]=='+' and (e[0]=='x' or e[2]=='x' or e[0]=='X' or e[2]=='X')):
            x += 1
        else : print("invalid format")
    print(x)
        
else:
    print("Invalid input")
