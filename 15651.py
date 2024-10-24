n, m = map(int, input().split())
ans = []

def back():
    if len(ans) == m: # 배열의 길이를 확인
        print(" ".join(map(str, ans))) # 1 2 3 이런 상태로 출력하기 위해
        return
    for i in range(1,n+1):
        ans.append(i)
        back()
        ans.pop()

back()