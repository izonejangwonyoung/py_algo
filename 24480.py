from sys import setrecursionlimit

count = 0


def dfs(graph, visited, start):
    global count
    count += 1
    visited[start] = count

    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, visited, i)


a, b, c = map(int, input().split())
setrecursionlimit(a + 10)  # 재귀 깊이 늘리기
visited = [False] * (a + 1)
graph = [[] for i in range(a + 1)]
# print(graph)
for i in range(b):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)
for i in range(1, a + 1):
    graph[i].sort(reverse=True)
# print(graph)
dfs(graph, visited, c)

# print(visited)
for i in range(1, a + 1):
    if visited[i]:
        print(visited[i])
    else:
        print(0)
