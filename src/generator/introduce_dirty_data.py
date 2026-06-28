import os
import random
import pandas as pd
import numpy as np

# =====================================================
# Configuration
# =====================================================

RAW_PATH = "data/raw"
DIRTY_PATH = "data/dirty"

os.makedirs(DIRTY_PATH, exist_ok=True)

random.seed(42)


# =====================================================
# Customers
# =====================================================

def dirty_customers():

    df = pd.read_csv(f"{RAW_PATH}/customers.csv")

    # Convert phone to string
    df["phone"] = df["phone"].astype(str)

    total = len(df)

    # 2% Missing Emails
    rows = random.sample(list(df.index), int(total * 0.02))
    df.loc[rows, "email"] = np.nan

    # 1% Blank First Name
    rows = random.sample(list(df.index), int(total * 0.01))
    df.loc[rows, "first_name"] = ""

    # 1% Invalid Phone
    rows = random.sample(list(df.index), int(total * 0.01))
    df.loc[rows, "phone"] = "123"

    # Duplicate Emails
    duplicate_rows = random.sample(list(df.index), 100)

    for row in duplicate_rows:
        source = random.choice(list(df.index))
        df.at[row, "email"] = df.at[source, "email"]

    df.to_csv(f"{DIRTY_PATH}/customers.csv", index=False)

    print("✅ Customers Dirty Data Added")


# =====================================================
# Products
# =====================================================

def dirty_products():

    df = pd.read_csv(f"{RAW_PATH}/products.csv")

    # Negative Price
    rows = random.sample(list(df.index), 20)
    df.loc[rows, "price"] *= -1

    # Zero Stock
    rows = random.sample(list(df.index), 30)
    df.loc[rows, "stock"] = 0

    # Wrong Categories
    replacements = {
        "Electronics": "Electroncs",
        "Fashion": "Fashon",
        "Sports": "Sportz"
    }

    for original, wrong in replacements.items():

        index = df[df["category"] == original].sample(
            min(5, len(df[df["category"] == original]))
        ).index

        df.loc[index, "category"] = wrong

    df.to_csv(f"{DIRTY_PATH}/products.csv", index=False)

    print("✅ Products Dirty Data Added")


# =====================================================
# Orders
# =====================================================

def dirty_orders():

    df = pd.read_csv(f"{RAW_PATH}/orders.csv")

    total = len(df)

    # Future Dates
    rows = random.sample(list(df.index), 100)
    df.loc[rows, "order_date"] = "2035-01-01"

    # Invalid Status
    rows = random.sample(list(df.index), 50)
    df.loc[rows, "order_status"] = "Unknown"

    # Missing Customer IDs
    rows = random.sample(list(df.index), 50)
    df.loc[rows, "customer_id"] = np.nan

    df.to_csv(f"{DIRTY_PATH}/orders.csv", index=False)

    print("✅ Orders Dirty Data Added")


# =====================================================
# Payments
# =====================================================

def dirty_payments():

    df = pd.read_csv(f"{RAW_PATH}/payments.csv")

    # Negative Amount
    rows = random.sample(list(df.index), 50)
    df.loc[rows, "amount"] *= -1

    # Invalid Payment Method
    rows = random.sample(list(df.index), 40)
    df.loc[rows, "payment_method"] = "Crypto"

    # Missing Payment Date
    rows = random.sample(list(df.index), 30)
    df.loc[rows, "payment_date"] = np.nan

    df.to_csv(f"{DIRTY_PATH}/payments.csv", index=False)

    print("✅ Payments Dirty Data Added")


# =====================================================
# Order Items
# =====================================================

def dirty_order_items():

    df = pd.read_csv(f"{RAW_PATH}/order_items.csv")

    # Negative Quantity
    rows = random.sample(list(df.index), 50)
    df.loc[rows, "quantity"] = -2

    # Zero Quantity
    rows = random.sample(list(df.index), 30)
    df.loc[rows, "quantity"] = 0

    # Invalid Product ID
    rows = random.sample(list(df.index), 30)
    df.loc[rows, "product_id"] = 999999

    df.to_csv(f"{DIRTY_PATH}/order_items.csv", index=False)

    print("✅ Order Items Dirty Data Added")


# =====================================================
# Summary
# =====================================================

def print_summary():

    print("\n===============================")
    print(" Dirty Data Summary")
    print("===============================")
    print("Customers  : Missing emails, blank names, invalid phones, duplicate emails")
    print("Products   : Negative prices, zero stock, wrong category names")
    print("Orders     : Future dates, invalid status, missing customer IDs")
    print("Payments   : Negative amount, invalid payment method, missing payment dates")
    print("OrderItems : Negative quantity, zero quantity, invalid product IDs")
    print("===============================\n")


# =====================================================
# Main
# =====================================================

def main():

    print("\nIntroducing Dirty Data...\n")

    dirty_customers()
    dirty_products()
    dirty_orders()
    dirty_payments()
    dirty_order_items()

    print_summary()

    print("🎉 Dirty datasets created successfully!")
    print(f"📁 Saved inside: {DIRTY_PATH}")


if __name__ == "__main__":
    main()