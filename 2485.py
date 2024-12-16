import sys

input=sys.stdin.readline


tree_list=[]
minus_list=[]
n=int(input())



def gcd(x,y):
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)


for _ in range(n):
    tree_list.append(int(input()))
for i in range(n-1):
    minus_list.append(abs(tree_list[i]-tree_list[i+1]))
minus_list=list(set(minus_list))
# print(minus_list)

while len(minus_list)!=1:
    a=minus_list.pop()
    b=minus_list.pop()
    value=gcd(a,b)
    minus_list.append(value)
value=minus_list[0]
answer=((abs(tree_list[-1]-tree_list[0])//value)-1)-(len(tree_list)-2)
print(answer)