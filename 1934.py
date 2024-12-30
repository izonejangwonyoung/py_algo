import math

t=int(input())



for i in range(t):
    a,b=map(int,input().split())
    temp=math.gcd(a,b)
    print((a*b)//temp)