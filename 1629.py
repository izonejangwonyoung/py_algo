a, b, c = map(int, input().split())

def calc(x,y,z):
    if y == 0:  # 종료 조건: 지수가 0이면 결과는 1
        return 1
    if y == 1:  # 종료 조건: 지수가 1이면 결과는 x % z
        return x % z
    half = calc(x, y // 2, z)  # 중복 계산 방지
    if y%2==1:
        return (half * half * x) % z
    if y%2==0:
        return (half * half) % z
    return result
result = calc(a, b, c)

print(result)


