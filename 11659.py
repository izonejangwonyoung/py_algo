import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)  # 크기 n+1로 설정

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + num_list[i - 1]



for _ in range(m):
    i, j = map(int, input().split())
    value=prefix_sum[j]-prefix_sum[i-1]
    print(value)
