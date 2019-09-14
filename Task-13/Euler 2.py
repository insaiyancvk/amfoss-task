def fibsum(n):
    a=0
    b=1
    f=0
    s=[]
    x=0
    while f<=n:
        f=a+b
        if f<=n:
            s.append(f)
        a=b
        b=f
    for i in range(len(s)):
        if s[i]%2==0:
           x=x+s[i]
    return x

def main():
    y=[]
    t=int(input())
    if t>=1 or t<=(10^5):
        for i in range(t):
            n=int(input())
            if n>=10 or n<=(4*(10^16)):
                y.append(fibsum(n))
        for j in range(len(y)):
            print(y[j])
main()
