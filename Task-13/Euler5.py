def hcf(a,b):
    c=0
    while(a!=0):
        c=a
        a=b%a
        b=c
    return b

def lcm(a,b):
    return (a*(b/hcf(a,b)))

if __name__=='__main__':
    a=[]
    t=int(input())
    for j in range(t):
        n=int(input())
        ans=1
        for i in range(2,n+1):
            ans=int(lcm(ans,i))
        a.append(ans)
    for k in range(len(a)):
        print(a[k])