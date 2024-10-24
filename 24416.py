n = int(input())

re_cnt=0
dy_cnt=0

def recursive_fibo(n):
    global re_cnt
    if n == 1 or n == 2:
        re_cnt += 1
        return 1
    else:
        return recursive_fibo(n - 1) + recursive_fibo(n - 2)


def dynamic_fibo(n):
    global dy_cnt
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        dy_cnt += 1

        f[i] = f[i - 1] + f[i - 2];
    return f[n]

recursive_fibo(n)
dynamic_fibo(n)
print(f"{re_cnt} {dy_cnt}")
