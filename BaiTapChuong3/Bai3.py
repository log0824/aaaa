def bucket_sort(arr, k):
    n = len(arr)
    output = [0]*n
    buckets = [[] for _ in range(k)]

    for i in range(0, n):
        tmp = arr[i] % k
        buckets[tmp].append(arr[i])
    
    for bucket in buckets:
        bucket.sort()

    res = 0
    i = k - 1
    while i >= 0:
        for s in buckets[i]:
            output[res] = s
            res += 1
        
        i -= 1

    for i in range(0, n):
        arr[i] = output[i]

if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    k = 4
    print("Dữ liệu gốc:", data)
    bucket_sort(data, k)
    print("Dữ liệu đã sắp xếp:", data)