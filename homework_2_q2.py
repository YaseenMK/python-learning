sales_records = [
{"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 5,
"region": "North"},
{"product": "Mouse", "category": "Electronics", "price": 25, "quantity": 50,
"region": "North"},
{"product": "Desk", "category": "Furniture", "price": 350, "quantity": 8,
"region": "South"},
{"product": "Chair", "category": "Furniture", "price": 150, "quantity": 20,
"region": "South"},
{"product": "Laptop", "category": "Electronics", "price": 999, "quantity": 3,
"region": "South"},
{"product": "Keyboard", "category": "Electronics", "price": 75, "quantity": 30, "region": "North"},
{"product": "Desk", "category": "Furniture", "price": 350, "quantity": 5,
"region": "North"},
{"product": "Monitor", "category": "Electronics", "price": 300, "quantity":
12, "region": "South"},
]


product_prices={record["product"]: record["price"] for record in sales_records}

print(product_prices)

print("\n")
print("=== Part A: Comprehensions ===")
# Only products with price > 100
expensive_products ={record["product"]:record["price"] for record in sales_records if record["price"] > 100}

print(expensive_products)

print("\n")
print("=== Part B: Aggregations ===")
price_category = {record["product"]:("Premium" if  record["price"] >= 300 else "Standard") for record in sales_records}

print(price_category)



total_by_category= {}

for record in sales_records:
    category = record["category"]
    revenue = record["price"] * record["quantity"]
    
    total_by_category[category] = total_by_category.get(category,0)+ revenue
    
print(total_by_category)


print("\n")
quantity_by_product = {}

for record in sales_records:
        product = record["product"]
        the_quantity= record["quantity"]
        
        
    
        quantity_by_product[product] = quantity_by_product.get(product, 0) + the_quantity

print(quantity_by_product)
    
    
    
    


    
    