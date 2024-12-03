import sys
input=sys.stdin.readline
n, k = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))
coin_list.sort(reverse=True)
# print(coin_list)
coin_count=0
index = 0
while True:
    if coin_list[index]<=k:
        coin_count+=k//coin_list[index]
        k= k- (k//coin_list[index])*coin_list[index]
    else:
        index+=1
    if k==0:
        break

print(coin_count)
