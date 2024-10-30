memo = {}
num = int(input())


# test_case = []
def calc(n):
    if n not in memo:
        memo[n] = 0
    if memo[n] != 0:
        return memo[n]
    if n == 1 or n == 2 or n == 3:
        return 1
    if n == 4 or n == 5:
        return 2
    memo[n] = calc(n - 1) + calc(n - 5)
    return memo[n]


for i in range(num):
    tmp = (int(input()))
    # calc(tmp)
    print(calc(tmp))
