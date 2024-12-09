n = int(input())
table = []
for _ in range(n):
    table.append(list(map(int, input().strip())))

result = []  # 결과를 저장할 리스트

def calc(x, y, n):
    borw = table[x][y]  # 첫 번째 칸의 색 (0: 하얀색, 1: 파란색)
    for i in range(x, x + n):
        for j in range(y, y + n):
            if borw != table[i][j]:  # 다른 색이 섞여 있다면
                result.append("(")  # 괄호 시작
                calc(x, y, n // 2)               # 1사분면
                calc(x, y + n // 2, n // 2)      # 2사분면
                calc(x + n // 2, y, n // 2)      # 3사분면
                calc(x + n // 2, y + n // 2, n // 2)  # 4사분면
                result.append(")")  # 괄호 종료
                return
    result.append(str(borw))  # 모든 칸이 같은 색이면 그 색 추가

calc(0, 0, n)
print("".join(result))  # 리스트를 문자열로 변환하여 출력
