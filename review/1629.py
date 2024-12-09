a, b, c = map(int, input().split())


def calc(x, y, z):
    if y == 0:  # y가 0이면 결과는 1
        return 1
    if y==1:
        return (x**1)%z
    half=calc(x, y // 2, z)*calc(x, y // 2, z)%z
    if y % 2 == 0:
        return half
    elif y % 2 == 1:
        return (half*x)%z
print(calc(a,b,c))