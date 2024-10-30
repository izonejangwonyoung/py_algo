n=int(input())
num_list=list(map(int,input().split()))

dp = [0] * n
dp[0] = num_list[0]
max_sum = dp[0]  # 첫 번째 값으로 초기화

# DP 계산
for i in range(1, n):
    dp[i] = max(dp[i - 1] + num_list[i], num_list[i])
    max_sum = max(max_sum, dp[i])  # 현재 최대 합 갱신

print(max_sum)