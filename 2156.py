n=int(input())
wine_list=[]

#dp_list=[0]*(n+1)
dp_list=[]
for i in range(1,n+1):
    wine_list.append(int(input()))
dp_list.append(0)
dp_list.append(wine_list[0])
#dp_list[1]=wine_list[0]
#dp_list[2]=wine_list[1]+wine_list[0]
if n==1:
    print(dp_list[1])

else:
    dp_list.append(wine_list[1] + wine_list[0])
    for i in range(3,n+1):
        dp_list.append(max(dp_list[i-1],dp_list[i-3]+wine_list[i-1]+wine_list[i-2],dp_list[i-2]+wine_list[i-1]))
        #이번 잔을 안 마시는 경우, 이번 잔을 마시고 바로 이전 잔도 마시는 경우, 이번 잔을 마시고 2개 전 잔을 마시는 경우
        #print(i,wine_list,dp_list)

    print(dp_list[-1])