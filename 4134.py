import math

a=int(input())



def calc(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

for _ in range(a):
    value=int(input())
    if value==0:
        print(2)
    elif value==1:
        print(2)
    else:
        while True:
            if calc(value):
                print(value)
                break
            value+=1