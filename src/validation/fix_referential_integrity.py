import os
import pandas as pd

os.makedirs("data/validated", exist_ok=True)

print("Loading cleaned datasets...")

customers = pd.read_csv("data/cleaned/customers.csv")
products = pd.read_csv("data/cleaned/products.csv")
orders = pd.read_csv("data/cleaned/orders.csv")
order_items = pd.read_csv("data/cleaned/order_items.csv")

# -----------------------------
# Valid IDs
# -----------------------------

valid_customers = set(customers["customer_id"])
valid_products = set(products["product_id"])

# -----------------------------
# Keep only orders with valid customers
# -----------------------------

orders = orders[
    orders["customer_id"].isin(valid_customers)
]

valid_orders = set(orders["order_id"])

# -----------------------------
# Keep only valid order items
# -----------------------------

order_items = order_items[
    order_items["order_id"].isin(valid_orders)
]

order_items = order_items[
    order_items["product_id"].isin(valid_products)
]

# -----------------------------
# Save validated files
# -----------------------------

customers.to_csv("data/validated/customers.csv", index=False)
products.to_csv("data/validated/products.csv", index=False)
orders.to_csv("data/validated/orders.csv", index=False)
order_items.to_csv("data/validated/order_items.csv", index=False)

print("\n========== VALIDATION COMPLETE ==========")
print(f"Customers   : {len(customers)}")
print(f"Products    : {len(products)}")
print(f"Orders      : {len(orders)}")
print(f"Order Items : {len(order_items)}")
print("Validated files saved to data/validated/")