print("Exercise 2")

def sum_natural(n):
    if n <0:
        return 0
    return n + sum_natural(n-1)

print(sum_natural(5))
print(sum_natural(10))
print(sum_natural(1))

print('\n')
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(1234))
print(count_digits(987654321))
print(count_digits(5)) 

print("\n")

def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0]!= s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("a"))

print("\n Exercise 4")
def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

print(power(2,5))
print(power(3,0))
print(power(5,3))

print("\n")
def generate_binary_strings(n):
    # Base case
    if n == 0:
        return [" "]

    # Recursive step
    smaller = generate_binary_strings(n - 1)
    result = []

    for s in smaller:
        result.append(s + "0")
        result.append(s + "1")

    return result

print(generate_binary_strings(2))
print(generate_binary_strings(1))


print("\n")

def subset_sum(nums, target):
    
    
    def helper(i, total):
        if total == target:
            return True
        if i == len(nums):
            return False
        
        return helper(i+1, total + nums[i]) or helper(i+1, total)

    return helper(0, 0)

print(subset_sum([3, 34, 4, 12, 5, 2], 9))
print(subset_sum([1, 2, 3, 4], 10))
print(subset_sum([1, 2, 3], 7))

print("\n Exercise 5")
def recursive_sum(arr, n):
    """
    Sum first n elements of array arr recursively.
    """
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

print(recursive_sum([1, 2, 3, 4], 4))

print("\n")

def binary_search(arr, target, left, right):
    
    if left > right:
        return -1

    mid = (left + right) // 2

    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
        
print("\n")

def edit_distance(s1, s2):
    
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    # Recursive step
    if s1[0] == s2[0]:
        return edit_distance(s1[1:], s2[1:])

    add = 1 + edit_distance(s1, s2[1:])
    removed = 1 + edit_distance(s1[1:], s2)
    changed = 1 + edit_distance(s1[1:], s2[1:])

    return min(add, removed, changed)