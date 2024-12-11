n,m=map(int,input().split())




tree_table=list(map(int,input().split()))



start=0
end=max(tree_table)
result=0
while start<=end:
    mid=(start+end)//2
    length=0

    for i in range(n):
        if tree_table[i]>mid:
            length+=tree_table[i]-mid
    # print(start,mid,end,length)
    if length>=m: #얻고자 하는 나무보다 너무 많이 얻어서 셋팅값을 줄여야함
        result=mid
        start=mid+1
    elif length<m:
        end=mid-1

print(result)
