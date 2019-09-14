def prime(n):
    c=0
    pf=[]
    y=[]
    d=0
    for i in range(1,n+1):
        if n%i==0:
            y.append(i)
    for j in range(len(y)):
        d=y[j]
        pf.append(prpr(d))
    return max(pf)

def prpr(d):
    c=0
    for i in range(1,d):
        if d%i==0:
            c=c+1
    if c==1:
        return d
    else:
        return 0
        

def main():
    m=[]
    t=int(input())
    if t>=1 or t<=10:
        for i in range(t):
            n=int(input())
            if n>=10 or n<=(10^12):
                m.append(prime(n))
        for j in range(len(m)):
            print(m[j])
main()
