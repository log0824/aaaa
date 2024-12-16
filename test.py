def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    len1, len2 = mid - left + 1, right - mid
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def timsort(arr):
    n = len(arr)
    MIN_RUN = 32

    # 1. Chia danh sách thành các Run
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # 2. Trộn các Run đã sắp xếp
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2

# Test thuật toán
arr = [5, 21, 7, 23, 19, 10, 3, 12, 15, 11, 1, 9]
print("Danh sách ban đầu:", arr)

timsort(arr)
print("Danh sách đã sắp xếp:", arr)
