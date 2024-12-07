n = int(input())

dp_list = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
curr_dp_list = []
if n == 1:
    print(sum(dp_list))
else:
    for i in range(0, n-1):
        for j in range(0, 10):
            if j == 0:
                curr_dp_list.append(dp_list[1])
            elif j == 9:
                curr_dp_list.append(dp_list[8])
            else:
                # print(j)
                curr_dp_list.append(dp_list[j - 1] + dp_list[j + 1])
        dp_list = curr_dp_list
        # print(curr_dp_list)
        curr_dp_list = []
        # print(dp_list)

    print(sum(dp_list)%1000000000)