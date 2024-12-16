def counting_sort(arr):
    m = 0
    n = len(arr)
    count = [0]* (max(arr) + 1)
    output = [0]*n

    for i in range(0, n):
        count[arr[i]] += 1
    
    for i in range(0, len(count)):
        if m < count[i]:
            m =  i
     
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    
    for i in range(0, n):
        arr[i] = output[i]

    tt=  0
    if n % 2 == 0:
        tt = (arr[n//2] + arr[n//2 - 1]) / 2
    else:
        tt = arr[n//2]

    return m, tt
    

if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66, 66, 2, 75, 75]
    print("Dữ liệu gốc:", data)
    m, tt = counting_sort(data)
    print(m)
    print(tt)
    print("Dữ liệu đã sắp xếp:", data)