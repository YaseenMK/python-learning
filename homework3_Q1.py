import numpy as np

zeros_arr = np.zeros(8)
print(zeros_arr)

print('\n')

ones_matrix = np.ones((3,4))
print(ones_matrix)


print('\n')

range_arr = np.arange(10, 51, 5)
print(range_arr)

print('\n')

linear_arr = np.linspace(0,2,9)
print(linear_arr)

a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3, 4, 5])

print(a + b)
print(a * b)
print(a ** 2)
print(a / b)

sum_A = np.sum(a)
print(sum_A)

mean_B = np.mean(b)
print(mean_B)
