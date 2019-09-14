def multiples(n):
    a=[]
    s=0
    for i in range(n):
        if i%3==0 or i%5==0:
            a.append(i)
    l=len(a)
    for i in range(l):
        s=s+a[i]
    return s


def main():
    s=[]
    t=int(input())
    if t>=1 or t<=(10^5):
        for i in range(t):
            n=int(input())
            if n>=1 or n<=(10^9):
                s.append(multiples(n))
        for i in range(len(s)):
                print(s[i])
main()
