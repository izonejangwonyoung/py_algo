n = int(input())

table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

result = [0, 0, 0]


def calc(x, y, n):
    number = table[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if number != table[i][j]:
                calc(x, y + n // 3, n // 3)
                calc(x, y +n * 2 // 3, n // 3)
                calc(x, y, n // 3)
                calc(x + n // 3, y + n // 3, n // 3)
                calc(x + n // 3, y + n * 2 // 3, n // 3)
                calc(x + n // 3, y, n // 3)
                calc(x + 2 * n // 3, y + n // 3, n // 3)
                calc(x + 2 * n // 3, y + n * 2 // 3, n // 3)
                calc(x + 2 * n// 3, y, n // 3)
                return
    if number == -1:
        result[0] += 1
    if number == 0:
        result[1] += 1
    if number == 1:
        result[2] += 1


calc(0, 0, n)
for i in range(len(result)):
    print(result[i])
