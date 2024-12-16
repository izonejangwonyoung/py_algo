
b,a=map(int,input().split())
d,c=map(int,input().split())

bunmo=a*c
bunja=(d*a)+(c*b)

def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)
tmp=gcd(bunmo,bunja)
while True:
    if tmp==1:
        print(bunja,bunmo)
        break
    else:
        bunmo=bunmo//tmp
        bunja=bunja//tmp
        tmp=gcd(bunmo,bunja)
