import sys
input=sys.stdin.readline
s = list(input().strip())  # 개행문자 제거 후 각 문자를 리스트로 변환
q=int(input())
prefix_sum = {char: [0] * len(s) for char in 'abcdefghijklmnopqrstuvwxyz'}
computed = {char: False for char in 'abcdefghijklmnopqrstuvwxyz'}  # 계산 여부 추적
print(computed)
print(prefix_sum)
for i in range(q):
    alphabet, l, r = input().split()
    l, r = int(l), int(r)  # 숫자 부분만 변환
    if computed[alphabet]==False:
        for j in range(0,len(s)):
            if s[j]==alphabet:
                prefix_sum[alphabet][j]=prefix_sum[alphabet][j-1]+1
            else:
                prefix_sum[alphabet][j]=prefix_sum[alphabet][j-1]
        computed[alphabet] = True


    if l==0:
        print(prefix_sum[alphabet][r])
        print(prefix_sum[alphabet])
    else:
        print(prefix_sum[alphabet][r]-prefix_sum[alphabet][l-1])
