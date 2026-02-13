import numpy as np

four_five = np.arange(1,21).reshape(4,5)

print(four_five)

print(f"The Shape:{four_five.shape}")

print(f"Number of dimensions:{four_five.ndim}")

print(f"Number of elements: {four_five.size}")

print(f"Data Type: {four_five.dtype}")

print(f"Total bytes:{four_five.nbytes}")

print("\n")
#  Part B
the_mean = np.mean(four_five)
print(the_mean)
st_dev = np.std(four_five)
The_minimum = np.amin(four_five)
print(The_minimum)
the_maximum = np.amax(four_five)
print(the_maximum)

flat = four_five.flatten()

print(flat)
