import os
import pandas as pd
from datetime import datetime

# ============================================
# Create cleaned folder
# ============================================

os.makedirs("data/cleaned", exist_ok=True)

# Valid Order Status
VALID_STATUS = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled",
    "Returned"
]


# ============================================
# Cleaning Function
# ============================================

def clean_orders():

    print("Loading Dirty Orders Dataset...")

    df = pd.read_csv("data/dirty/orders.csv")

    original_rows = len(df)

    # -----------------------------------
    # Remove Duplicate Order IDs
    # -----------------------------------

    df.drop_duplicates(
        subset="order_id",
        keep="first",
        inplace=True
    )

    # -----------------------------------
    # Remove Missing Customer IDs
    # -----------------------------------

    df.dropna(subset=["customer_id"], inplace=True)

    # Convert customer_id back to integer
    df["customer_id"] = df["customer_id"].astype(int)

    # -----------------------------------
    # Convert order_date to datetime
    # -----------------------------------

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    # Remove invalid dates
    df.dropna(subset=["order_date"], inplace=True)

    # -----------------------------------
    # Remove Future Dates
    # -----------------------------------

    today = pd.Timestamp.today().normalize()

    df = df[df["order_date"] <= today]

    # -----------------------------------
    # Fix Invalid Order Status
    # -----------------------------------

    df.loc[
        ~df["order_status"].isin(VALID_STATUS),
        "order_status"
    ] = "Pending"

    # -----------------------------------
    # Remove Negative Total Amount
    # -----------------------------------

    df["total_amount"] = df["total_amount"].abs()

    # -----------------------------------
    # Convert Date Back to String
    # -----------------------------------

    df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

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
        "data/cleaned/orders.csv",
        index=False
    )

    cleaned_rows = len(df)

    removed = original_rows - cleaned_rows

    print("\n========== Orders Cleaning Report ==========")

    print(f"Original Records : {original_rows}")

    print(f"Clean Records    : {cleaned_rows}")

    print(f"Removed Records  : {removed}")

    print("Saved to data/cleaned/orders.csv")

    print("============================================")


# ============================================
# Main
# ============================================

def main():

    clean_orders()


if __name__ == "__main__":
    main()