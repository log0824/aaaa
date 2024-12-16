def sum_digit(n):
    return sum(int(digit) for digit in str(n))

def count_sort(arr, digit_sum):
    n = len(arr)
    count = [0] * 100
    output = [0]*n

    for s in digit_sum:
        count[s] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        s = digit_sum[i]
        output[count[s] - 1] = arr[i]
        count[s] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = output[i]

def sort(arr):
    digit_sum = [sum_digit(num) for num in arr]

    count_sort(arr, digit_sum)
    n = len(arr)
    i = 0
    while i < n:
        j = i
        while j < n and sum_digit(arr[j]) == sum_digit(arr[i]):
            j += 1
        arr[i:j] = sorted(arr[i:j])
        i = j


if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Dữ liệu gốc:", data)
    sort(data)
    print("Dữ liệu đã sắp xếp:", data)
