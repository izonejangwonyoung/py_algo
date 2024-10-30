N = int(input())
dp = [0] * (N + 1)  # DP 테이블 초기화

# DP 계산
for i in range(2, N + 1):
    # 기본적으로 이전 값에서 1을 빼는 경우로 초기화
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어질 때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어 떨어질 때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])  # N을 1로 만드는 최소 연산 횟수
