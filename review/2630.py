result = [0, 0]
n = int(input())

table = []

for _ in range(n):
    table.append(list(map(int, input().split())))


def calc(x, y, z):
    standard = table[x][y]
    for i in range(x, x + z):
        for j in range(y, y + z):
            if standard != table[i][j]:
                calc(x, y, z // 2)
                calc(x + z // 2, y, z // 2)
                calc(x, y + z // 2, z // 2)
                calc(x + z // 2, y + z // 2, z // 2)
                return

    if standard == 1:
        result[0] += 1
    else:
        result[1] += 1


calc(0, 0, n)
print(result[1])
print(result[0])
