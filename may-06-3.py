# task:3
# * *
# * *
# * * * * * *
# * *
# * *
import math
num=7
flag=True
for i in range(num,0,-1):
    res=""
    for j in range(1,3):
       if i==math.ceil(num/2) and flag==True:
              res+="* "*num 
              flag=False
              break
       else:
           res+="*"+" "
    print(res)   

def print_star_pattern():
    pattern = [
        "* *",
        "* *",
        "* * * * * *",
        "* *",
        "* *"
    ]
    for line in pattern:
        print(line)

print_star_pattern()
      
    

