print("Recursion Question 2")

import random, time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


nums = [random.randint(1, 1000000) for _ in range(1000000)]  # smaller so it runs fast

start = time.time()
sorted_nums = merge_sort(nums)
end = time.time()

print("Time:", end - start)