import os
import pandas as pd

# ============================================
# Create cleaned folder
# ============================================

os.makedirs("data/cleaned", exist_ok=True)


# ============================================
# Cleaning Function
# ============================================

def clean_order_items():

    print("Loading Dirty Order Items Dataset...")

    # Load datasets
    df = pd.read_csv("data/dirty/order_items.csv")
    products = pd.read_csv("data/cleaned/products.csv")

    original_rows = len(df)

    # -----------------------------------
    # Remove Duplicate Order Item IDs
    # -----------------------------------

    df.drop_duplicates(
        subset="order_item_id",
        keep="first",
        inplace=True
    )

    # -----------------------------------
    # Remove Invalid Product IDs
    # -----------------------------------

    valid_products = set(products["product_id"])

    df = df[df["product_id"].isin(valid_products)]

    # -----------------------------------
    # Remove Zero or Negative Quantity
    # -----------------------------------

    df = df[df["quantity"] > 0]

    # -----------------------------------
    # Remove Negative Unit Price
    # -----------------------------------

    df["unit_price"] = df["unit_price"].abs()

    # -----------------------------------
    # Recalculate Line Total
    # -----------------------------------

    df["line_total"] = (
        df["quantity"] * df["unit_price"]
    ).round(2)

    # -----------------------------------
    # Reset Index
    # -----------------------------------

    df.reset_index(
        drop=True,
        inplace=True
    )

    # -----------------------------------
    # Save Clean Dataset
    # -----------------------------------

    df.to_csv(
        "data/cleaned/order_items.csv",
        index=False
    )

    cleaned_rows = len(df)

    removed = original_rows - cleaned_rows

    print("\n========== Order Items Cleaning Report ==========")

    print(f"Original Records : {original_rows}")
    print(f"Clean Records    : {cleaned_rows}")
    print(f"Removed Records  : {removed}")

    print("Saved to data/cleaned/order_items.csv")

    print("=================================================")


# ============================================
# Main
# ============================================

def main():

    clean_order_items()


if __name__ == "__main__":
    main()