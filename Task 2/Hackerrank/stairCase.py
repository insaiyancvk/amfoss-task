n = int(input("Enter the limit of the stairs : "))
for i in range(n+1):
    print(" " * (n-i) + "#" * i)
