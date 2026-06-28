import pandas as pd
import random

# -----------------------------
# Load Existing Data
# -----------------------------

products_df = pd.read_csv("data/raw/products.csv")
orders_df = pd.read_csv("data/raw/orders.csv")


# -----------------------------
# Generate Order Items
# -----------------------------

def generate_order_items():

    order_items = []
    order_item_id = 1

    # Convert product dataframe into dictionary for quick lookup
    product_lookup = products_df.set_index("product_id").to_dict("index")

    for _, order in orders_df.iterrows():

        order_id = order["order_id"]

        # Every order will have 1 to 5 products
        number_of_products = random.randint(1, 5)

        # Pick unique products
        selected_products = random.sample(
            list(product_lookup.keys()),
            number_of_products
        )

        for product_id in selected_products:

            quantity = random.randint(1, 5)

            unit_price = product_lookup[product_id]["price"]

            order_items.append({
                "order_item_id": order_item_id,
                "order_id": order_id,
                "product_id": product_id,
                "quantity": quantity,
                "unit_price": unit_price,
                "line_total": round(quantity * unit_price, 2)
            })

            order_item_id += 1

    return pd.DataFrame(order_items)


# -----------------------------
# Save CSV
# -----------------------------

def save_order_items(df):

    df.to_csv(
        "data/raw/order_items.csv",
        index=False
    )


# -----------------------------
# Main
# -----------------------------

def main():

    print("Generating Order Items...")

    order_items_df = generate_order_items()

    save_order_items(order_items_df)

    print(f"✅ Successfully generated {len(order_items_df)} order items.")

    print("📁 File saved to: data/raw/order_items.csv")


if __name__ == "__main__":
    main()