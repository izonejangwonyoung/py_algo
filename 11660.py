import sys
input=sys.stdin.readline
n, m = map(int, input().split())
# graph=[][]
graph = []
prefix_sum = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:  # 시작점
            prefix_sum[i][j] = graph[i][j]
        if i == 0:
            prefix_sum[i][j] = graph[i][j] + prefix_sum[i][j - 1]

        if j == 0:
            prefix_sum[i][j] = graph[i][j] + prefix_sum[i-1][j]

        else:
            prefix_sum[i][j] = graph[i][j] + prefix_sum[i][j - 1] + prefix_sum[i - 1][j] - prefix_sum[i - 1][j - 1]

# print(prefix_sum," ")
def safe_prefix_sum(i,j):
    if i<0 or j<0:
        return 0
    return prefix_sum[i][j]
for _ in range(m):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    # if x1 == 0 and y1 == 0:
    #     print(safe_prefix_sum(x2, y2))
    # elif x1 == x2 and y1 == y2:
    #     print(graph[x2][y2])
    # elif x1 == x2:
    #     print(safe_prefix_sum(x2, y2) - safe_prefix_sum(x1 - 1, y2))
    # elif y1 == y2:
    #     print(safe_prefix_sum(x2, y2) - safe_prefix_sum(x1, y2))
    # else:
    print(
            safe_prefix_sum(x2, y2)
            - safe_prefix_sum(x1 - 1, y2)
            - safe_prefix_sum(x2, y1 - 1)
            + safe_prefix_sum(x1 - 1, y1 - 1)
        )