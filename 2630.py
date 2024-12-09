n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().split())))
result=[]

def calc(x, y, n):
    color = table[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != table[i][j]:
                calc(x, y, n // 2)
                calc(x, y + n // 2, n // 2)
                calc(x + n // 2, y, n // 2)
                calc(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

calc(0, 0, n)
print(result.count(0))
print(result.count(1))