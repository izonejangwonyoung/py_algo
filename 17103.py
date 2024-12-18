import sys
input = sys.stdin.readline

# 소수 생성 함수
def get_primes(limit):
    tmp_list = list(range(2, limit + 1))  # 2부터 limit까지의 리스트
    end = int(limit**0.5) + 1  # √limit까지만 검사

    for i in range(2, end):
        if tmp_list[i - 2] == 0:  # 이미 제거된 값은 건너뛴다
            continue
        for j in range(i * i, limit + 1, i):  # 배수 제거
            tmp_list[j - 2] = 0

    # 0을 제거하여 소수 리스트 반환
    return [num for num in tmp_list if num != 0]

# 두 소수의 합 계산 함수
def calc(x):
    primes = get_primes(x)  # x 이하의 소수를 구함
    count = 0

    # 두 소수의 합 계산
    for i in range(len(primes)):
        for j in range(i, len(primes)):  # 중복 계산 방지
            if primes[i] + primes[j] == x:
                count += 1

    print(count)

# 실행 파트
t = int(input())
for _ in range(t):
    tmp = int(input())
    calc(tmp)
