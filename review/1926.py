paint=[]


n,m=map(int,input().split())

for _ in range(n):
    paint.append(list(map(int,input().split())))

print(paint)
paint_count=0
max_paint_area=0
search_complete=set()
def calc(x,y):
    area = 0
    stack = [(x, y)]
    search_complete.add((x, y))
    # print(x,y)

    while stack:
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        cx,cy=stack.pop()
        area+=1
        for dx,dy in direction:
            nx=cx+dx
            ny=cy+dy
            if 0<=nx<n and 0<=ny<m and (nx,ny) not in search_complete and paint[nx][ny]==1:
                stack.append((nx,ny))
                search_complete.add((nx,ny))
    return area

max_area=0
for i in range(n):
    for j in range(m):
        if paint[i][j]==1 and (i,j) not in search_complete:
            print(i,j)
            paint_count+=1
            max_area=max(max_area,calc(i,j))
            print(max_area)

print(paint_count)
print(max_area)
