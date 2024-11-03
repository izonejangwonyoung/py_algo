n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
ans = []
checked = [False] * n


def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    last_num = 0
    for i in range(n):

        if checked[i] == False and last_num != num_list[i] and (len(ans)==0 or ans[-1] <= num_list[i]):
            checked[i] = True
            last_num = num_list[i]
            ans.append(num_list[i])
            back()
            checked[i] = False
            ans.pop()


back()
