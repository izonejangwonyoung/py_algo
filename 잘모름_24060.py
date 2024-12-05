from heapq import merge

n, k = map(int, input().split())
array = list(map(int, input().split()))


def merge_sort_with_k(n, k, array):
    count = 0  # 저장 횟수를 추적
    kth_value = -1  # K번째 저장되는 값을 저장

    def merge_sort(array, left, right):
        nonlocal count, kth_value
        if left >= right:
            return

        mid = (left + right) // 2
        merge_sort(array, left, mid)  # 왼쪽 정렬
        merge_sort(array, mid + 1, right)  # 오른쪽 정렬
        merge(array, left, mid, right)  # 병합 단계

    def merge(array, left, mid, right):
        nonlocal count, kth_value
        tmp = []
        i, j = left, mid + 1

        while i <= mid and j <= right:
            if array[i] <= array[j]:
                tmp.append(array[i])
                i += 1
            else:
                tmp.append(array[j])
                j += 1
            count += 1
            if count == k:  # K번째 저장된 값
                kth_value = tmp[-1]

        while i <= mid:
            tmp.append(array[i])
            i += 1
            count += 1
            if count == k:
                kth_value = tmp[-1]

        while j <= right:
            tmp.append(array[j])
            j += 1
            count += 1
            if count == k:
                kth_value = tmp[-1]

        # 결과를 원래 배열에 반영
        for t in range(len(tmp)):
            array[left + t] = tmp[t]

    merge_sort(array, 0, n - 1)  # 병합 정렬 호출
    return kth_value if count >= k else -1  # K번째 저장된 값 또는 -1 반환


print(merge_sort_with_k(n, k, array))
