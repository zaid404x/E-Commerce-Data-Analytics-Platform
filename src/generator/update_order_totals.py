import pandas as pd


def update_order_totals():

    print("Loading datasets...")

    # Load datasets
    orders_df = pd.read_csv("data/raw/orders.csv")
    order_items_df = pd.read_csv("data/raw/order_items.csv")

    print("Calculating total amount for each order...")

    # Calculate total for every order
    totals = (
        order_items_df
        .groupby("order_id")["line_total"]
        .sum()
        .reset_index()
    )

    totals.rename(columns={"line_total": "total_amount"}, inplace=True)

    # Remove old random total
    orders_df.drop(columns=["total_amount"], inplace=True)

    # Merge actual total
    orders_df = orders_df.merge(
        totals,
        on="order_id",
        how="left"
    )

    # Round values
    orders_df["total_amount"] = orders_df["total_amount"].round(2)

    # Save updated file
    orders_df.to_csv(
        "data/raw/orders.csv",
        index=False
    )

    print("✅ Orders updated successfully!")
    print("📁 orders.csv now contains actual order totals.")


def main():
    update_order_totals()


if __name__ == "__main__":
    main()