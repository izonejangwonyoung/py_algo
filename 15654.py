from logging import makeLogRecord

n, m = map(int, input().split())
num_list=sorted(list(map(int, input().split())))
ans=[]

def back():
    if len(ans)==m:
        print(" ".join(map(str, ans)))  # 1 2 3 이런 상태로 출력하기 위해
        return
    for i in num_list:
        if len(ans) == 0 or (i not in ans and ans[-1] < i):
            ans.append(i)
            back()
            ans.pop()


back()
