matrix_a=[
]
matrix_b=[]
n,m=map(int,input().split())
for _ in range(n):
    matrix_a.append(list(map(int,input().split())))
m,k=map(int,input().split())
for _ in range(m):
    matrix_b.append(list(map(int,input().split())))

matrix_c=[[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for o in range(m):
            matrix_c[i][j]+=matrix_a[i][o]*matrix_b[o][j]
for i in range(n):
    for j in range(k):
        print(matrix_c[i][j], end=" ")
    print("")