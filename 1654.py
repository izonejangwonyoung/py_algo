import sys
input=sys.stdin.readline
n,k= map(int,input().split())

lan_list=[]

for _ in range(n):
    lan_list.append(int(input()))

# print(*lan_list,sep='\n')

start=1
end=max(lan_list)
mid = (start + end) // 2
result = 0

while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(n):
        count+=lan_list[i]//mid
    # print("start",start,"end",end,"mid",mid,"count",count)
    if count>=k:    #mid를 중심으로 오른쪽 리스트를 선택해줘야함
        result=mid
        start=mid+1
    elif count<k:
        end=mid-1


print(result)