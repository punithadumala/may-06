# task:2
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(1,n+1):
    if i==1:
        print("* "*n)
    else:
        print("* "*(n-i+1)) 
        
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("* ",end="")
    print()           