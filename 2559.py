import sys
input=sys.stdin.readline
n,k=map(int,input().split())
temperature_list=list(map(int,input().split()))

prefix_sum=[0]*(n-k+1)


for i in range(0,n-k+1):
    if i==0:
        for p in range(0,k):
            prefix_sum[0] += temperature_list[p]
    else:
        prefix_sum[i]=prefix_sum[i-1]+temperature_list[k+i-1]-temperature_list[i-1]
    # print(prefix_sum)
print(max(prefix_sum))