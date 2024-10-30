ans = []
n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))


def back():
    if len(ans)==m:
        print(" ".join(map(str, ans)))
        return  #그 전 함수로 돌아감
    for i in num_list:
            ans.append(i)
            back()
            ans.pop()
back()