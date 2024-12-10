n = int(input())
table = []

for _ in range(0, n):
    table.append(list(map(int, input().split())))


result = [0, 0, 0]


def calc(x, y, z):
    standard = table[x][y]
    for i in range(x, x + z):
        for j in range(y, y + z):
            if standard != table[i][j]:
                calc(x, y, z // 3)
                calc(x + z // 3, y, z // 3)
                calc(x + 2 * z // 3, y, z // 3)
                calc(x, y + z // 3, z // 3)
                calc(x + z // 3, y + z // 3, z // 3)
                calc(x + 2 * z // 3, y + z // 3, z // 3)
                calc(x, y + 2 * z // 3, z // 3)
                calc(x + z // 3, y + 2 * z // 3, z // 3)
                calc(x + 2 * z // 3, y + 2 * z // 3, z // 3)
                return

    if standard == -1:
        result[0] += 1
    elif standard == 0:
        result[1] += 1
    elif standard == 1:
        result[2] += 1


calc(0, 0, n)
for l in range(len(result)):
    print(result[l],end='\n')