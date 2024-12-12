import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

curr_max_area = 0
checked_coordinate = set()  # 방문 좌표를 저장할 집합
paint_count = 0

def check_paint(x, y):
    stack = [(x, y)]
    checked_coordinate.add((x, y))
    area = 0

    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while stack:
        # print(stack)  # 디버그용 출력 (주석처리)
        cx, cy = stack.pop()
        # print(cx, cy)  # 디버그용 출력 (주석처리)
        area += 1

        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1 and (nx, ny) not in checked_coordinate:
                stack.append((nx, ny))
                checked_coordinate.add((nx, ny))
    return area

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and (i, j) not in checked_coordinate:
            paint_count += 1
            curr_max_area = max(curr_max_area, check_paint(i, j))

print(paint_count)
print(curr_max_area)
