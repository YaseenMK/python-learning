import numpy as np

arr = np.arange(1,25)

print(arr)
print("\n")
arr_foursix = np.arange(1,25).reshape(4,6)
print("\n")
print(arr_foursix)


arr_3d = np.arange(1,25).reshape(2,3,4)
print("\n")
print(arr_3d)

flat= arr_3d.flatten()
print("\n")
print(flat)

print("\n")

# Rows: products (Apple, Banana, Orange)
# Columns: stores (Store1, Store2, Store3, Store4)
prices = np.array([
[1.20, 1.50, 1.30, 1.40], # Apple
[0.50, 0.60, 0.55, 0.45], # Banana
[0.80, 0.90, 0.85, 0.75] # Orange
])

print(prices * 0.9)
print("\n")
print(prices + 0.10)
print("\n")


#The stores have different tax rates: [0.08, 0.06, 0.07, 0.05]. Calculate the final price with tax for each product in each store. 


differnt_tax = np.array([0.08, 0.06, 0.07, 0.05])

priceof_each = prices * (1 + differnt_tax)

print(priceof_each)

the_mean = prices.mean(axis=1, keepdims=True)

print(the_mean - prices)



