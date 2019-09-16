def mult(n):
    return sum(n,3) + sum(n,5) - sum(n,15)

def sum(n,k):
    d = n//k
    return k * (d*(d+1)) // 2

if __name__=='__main__':
    t=int(input().strip())
    for i in range(t):
        n=int(input().strip())
        print(mult(n-1))
