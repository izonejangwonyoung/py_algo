a,b=map(int,input().split())




def calc(x,y):

    while True:
        value=y%x
        if value==0:
            # print(x,y)
            break
        else:
            y=x
            x=value
    return x

gcd=calc(a,b)

print((a*b)//gcd)
