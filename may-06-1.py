N=5
for i in range(N,0,-1):
    for j in range(i):
        print(i,end="")
    print()


n=5
for i in range(0,n):
    if i==0:
        print(n*str(n))
    else:
        print((n-i)*str(n-i))    
