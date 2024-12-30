n=int(input())



temp=n//4
if n%4==0:
    temp = n // 4
else:
    temp=(n//4)+1

for i in range(temp):
    print("long",end=' ')

print("int")