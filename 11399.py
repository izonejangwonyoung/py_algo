import sys

input = sys.stdin.readline
n = int(input())
time_list = list(map(int, input().split()))

time_list.sort()
sum=0
for i in range(0,n+1):
    for j in range(0,i):
        # print(j)
        # print(j)
        sum+=time_list[j]


print(sum)