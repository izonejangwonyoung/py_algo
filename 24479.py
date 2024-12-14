import sys
from collections import defaultdict
input=sys.stdin.readline
sys.setrecursionlimit(300000)

n, m, r = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 양방향 간선

# 인접 정점들을 사전식 순서로 정렬
for key in graph:
    graph[key].sort()
visited = [0] * (n + 1)
order=0
def dfs(node):    #v는 정점 집합,e는 간선 집합, r은 시작 정점
    global order
    order += 1
    visited[node] = order
    for tmp in graph[node]:
        # print(i,graph[i-1])
        if visited[tmp] == 0:
            dfs(tmp)

dfs(r)
# print(visited)
for i in range(1, n + 1):
    print(visited[i])  # 방문하지 않은 정점은 기본값 0이 출력됨