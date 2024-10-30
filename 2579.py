list_num=[0]
n=int(input())
dp=[0]*(n+1)
for i in range(n):
    list_num.append(int(input()))

dp[1] = list_num[1]
if n > 1:
    dp[2] = list_num[1] + list_num[2]
if n > 2:
    dp[3] = max(list_num[1] + list_num[3], list_num[2] + list_num[3])
for i in range(4,n+1):
    dp[i]=max(dp[i-3]+list_num[i-1],dp[i-2])+list_num[i]
print(dp[n])