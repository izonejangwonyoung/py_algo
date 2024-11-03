n, m = map(int, input().split())
list_num = sorted(list(map(int, input().split())))
ans = []

checked = [False] * n



def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    last_num = 0
    for i in range(n):
        # 각 호출 단계에서 중복된 숫자는 건너뛰도록 설정
        if last_num != list_num[i]:
            ans.append(list_num[i])
            last_num = list_num[i]  # 현재 호출 단계에서 사용된 숫자를 기록
            back()
            ans.pop()

back()