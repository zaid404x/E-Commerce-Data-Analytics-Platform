import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker("en_IN")

# Number of orders to generate
NUM_ORDERS = 50000

# Total customers generated
TOTAL_CUSTOMERS = 10000

# Order status options
ORDER_STATUS = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled",
    "Returned"
]


def generate_order_date():
    """
    Generate a random order date within the last 2 years.
    """
    return fake.date_between(start_date="-2y", end_date="today")


def generate_order_status():
    """
    Randomly assign an order status.
    """
    return random.choice(ORDER_STATUS)


def generate_total_amount():
    """
    Generate a temporary order amount.
    (Later this will be calculated from order_items)
    """
    return round(random.uniform(200, 100000), 2)


def generate_orders():
    """
    Generate order dataset.
    """
    orders = []

    for order_id in range(1, NUM_ORDERS + 1):

        order = {
            "order_id": order_id,
            "customer_id": random.randint(1, TOTAL_CUSTOMERS),
            "order_date": generate_order_date(),
            "order_status": generate_order_status(),
            "total_amount": generate_total_amount()
        }

        orders.append(order)

    return pd.DataFrame(orders)


def save_orders(df):
    """
    Save orders to CSV.
    """
    df.to_csv("data/raw/orders.csv", index=False)


def main():

    print("Generating orders...")

    orders_df = generate_orders()

    save_orders(orders_df)

    print(f"✅ Successfully generated {len(orders_df)} orders.")
    print("📁 File saved to: data/raw/orders.csv")


if __name__ == "__main__":
    main()