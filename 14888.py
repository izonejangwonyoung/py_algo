def dfs(depth, current_result, add, subtract, multiply, divide):
    global max_value, min_value

    # 모든 숫자를 사용한 경우
    if depth == N:
        max_value = max(max_value, current_result)
        min_value = min(min_value, current_result)
        return

    # 연산자 사용 가능 여부에 따라 백트래킹
    if add > 0:
        dfs(depth + 1, current_result + numbers[depth], add - 1, subtract, multiply, divide)

    if subtract > 0:
        dfs(depth + 1, current_result - numbers[depth], add, subtract - 1, multiply, divide)

    if multiply > 0:
        dfs(depth + 1, current_result * numbers[depth], add, subtract, multiply - 1, divide)

    if divide > 0:
        # 나눗셈은 정수 몫만 취한다.
        if current_result < 0:
            dfs(depth + 1, -(-current_result // numbers[depth]), add, subtract, multiply, divide - 1)
        else:
            dfs(depth + 1, current_result // numbers[depth], add, subtract, multiply, divide - 1)


# 입력 처리
N = int(input())
numbers = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

# 최댓값과 최솟값 초기화
max_value = -float('inf')
min_value = float('inf')

# DFS 시작
dfs(1, numbers[0], add, subtract, multiply, divide)

# 결과 출력
print(max_value)
print(min_value)