n=int(input())
table=[]
for _ in range(n):
    table.append(list(map(int,input().rstrip())))
result=[]
def calc(x,y,n):
    color = table[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != table[i][j]:
                result.append("(")
                calc(x,y,n//2)
                calc(x,y+n//2,n//2)
                calc(x+n//2,y,n//2)
                calc(x+n//2,y+n//2,n//2)
                result.append(")")
                return
    if color==1:
        result.append(1)
    elif color==0:
        result.append(0)

calc(0,0,n)
for l in range(len(result)):
    print(result[l],end='')