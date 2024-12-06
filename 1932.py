import sys

input = sys.stdin.readline

n = int(input())

tri_list = []
dp_list = []
for i in range(n):
    tri_list.append(list(map(int, input().split())))

if 0 < n <= 2:
    if n == 1:
        print(max(tri_list[0]))
    if n==2:
        result = max(tri_list[0][0] + tri_list[1][0], tri_list[0][0] + tri_list[1][1])
        print(result)
else:
    dp_list.append(tri_list[0][0] + tri_list[1][0])
    dp_list.append(tri_list[0][0] + tri_list[1][1])

    curr_dp_list = []
    # print(dp_list)
    for i in range(2, n):
        curr_dp_list = []
        # print(i,"번쨰 라인 계산")
        for j in range(0, i + 1):
            # print(tri_list[i],"에서",j,"번쨰 수 갖고 계산중")
            if j == 0:  # 맨 왼쪽
                curr_dp_list.append(dp_list[j] + tri_list[i][j])
            elif j == i:  # 맨 오른쪽
                curr_dp_list.append(dp_list[j - 1] + tri_list[i][j])
            else:  # 가운데
                curr_dp_list.append(max(dp_list[j - 1], dp_list[j]) + tri_list[i][j])
        dp_list = curr_dp_list
    # print(dp_list)
    print(max(curr_dp_list))
