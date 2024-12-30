n,m=map(int,input().split())
basket_list=[0]*n

for _ in range(m):
    i,j,k=map(int,input().split())
    for o in range(i-1,j):
        basket_list[o]=k
    # print(basket_list)
for _ in range(len(basket_list)):
    print(basket_list[_],end=' ')