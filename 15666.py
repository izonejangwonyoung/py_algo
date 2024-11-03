n, m = map(int, input().split())
list_num = sorted(list(map(int, input().split())))
ans = []


def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    last_num = 0
    for i in range(n):
        if last_num != list_num[i] and (len(ans) == 0 or ans[-1] <= list_num[i]):
            ans.append(list_num[i])
            last_num = list_num[i]
            back()
            ans.pop()


back()
