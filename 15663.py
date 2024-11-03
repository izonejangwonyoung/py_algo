n, m = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
ans = []
checked=[False]*n
global last_word

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
        return
    temp = 0

    for i in range(n):
        if checked[i]==False and temp!=num_list[i]:
            checked[i]=True
            ans.append(num_list[i])
            temp=num_list[i]
            # last_word = i
            back()
            checked[i]=False
            ans.pop()


back()
# print(ans)
