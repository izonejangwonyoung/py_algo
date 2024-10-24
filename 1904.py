n=int(input())

memo = {}
def calc(n):
    memo[1]=1
    memo[2]=2
    for i in range(3, n + 1):
        memo[i] = (memo[i - 1] + memo[i - 2])%15746
    return memo[n]
print(calc(n))
