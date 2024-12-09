
n = int(input())
n_list = sorted(list(map(int, input().split())))  # set 사용

m = int(input())
m_list = list(map(int, input().split()))


def calc(num, target_list):

    start=0
    end=len(target_list)-1


    while start<=end:
        mid_index = (start + end) // 2
        mid = target_list[mid_index]
        if mid>num:
            end=mid_index-1
        elif mid<num:
            start=mid_index+1
        if mid==num:
            return 1
    return 0


for i in range(len(m_list)):
    num = m_list[i]
    print(calc(num, n_list))
