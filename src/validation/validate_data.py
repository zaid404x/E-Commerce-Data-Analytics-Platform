import os
import pandas as pd
import re

# ============================================
# Create reports folder
# ============================================

os.makedirs("reports", exist_ok=True)

REPORT_FILE = "reports/validation_report.txt"


# ============================================
# Email Validation
# ============================================

def valid_email(email):

    if pd.isna(email):
        return False

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return bool(re.match(pattern, str(email)))


# ============================================
# Main Validation
# ============================================

def validate():

    customers = pd.read_csv("data/cleaned/customers.csv")
    products = pd.read_csv("data/cleaned/products.csv")
    orders = pd.read_csv("data/cleaned/orders.csv")
    order_items = pd.read_csv("data/cleaned/order_items.csv")

    report = []

    report.append("=" * 50)
    report.append("DATA VALIDATION REPORT")
    report.append("=" * 50)

    # ---------------------------------------
    # Customers
    # ---------------------------------------

    report.append("\nCUSTOMERS")

    duplicate_customer_ids = customers["customer_id"].duplicated().sum()

    duplicate_emails = customers["email"].duplicated().sum()

    invalid_emails = (~customers["email"].apply(valid_email)).sum()

    report.append(f"Duplicate Customer IDs : {duplicate_customer_ids}")
    report.append(f"Duplicate Emails       : {duplicate_emails}")
    report.append(f"Invalid Emails         : {invalid_emails}")

    # ---------------------------------------
    # Products
    # ---------------------------------------

    report.append("\nPRODUCTS")

    duplicate_products = products["product_id"].duplicated().sum()

    negative_prices = (products["price"] < 0).sum()

    missing_category = products["category"].isna().sum()

    report.append(f"Duplicate Product IDs  : {duplicate_products}")
    report.append(f"Negative Prices        : {negative_prices}")
    report.append(f"Missing Category       : {missing_category}")

    # ---------------------------------------
    # Orders
    # ---------------------------------------

    report.append("\nORDERS")

    duplicate_orders = orders["order_id"].duplicated().sum()

    missing_customer = (~orders["customer_id"].isin(
        customers["customer_id"])).sum()

    report.append(f"Duplicate Orders       : {duplicate_orders}")
    report.append(f"Missing Customers      : {missing_customer}")

    # ---------------------------------------
    # Order Items
    # ---------------------------------------

    report.append("\nORDER ITEMS")

    invalid_order = (~order_items["order_id"].isin(
        orders["order_id"])).sum()

    invalid_product = (~order_items["product_id"].isin(
        products["product_id"])).sum()

    negative_quantity = (order_items["quantity"] <= 0).sum()

    report.append(f"Invalid Orders         : {invalid_order}")
    report.append(f"Invalid Products       : {invalid_product}")
    report.append(f"Negative Quantity      : {negative_quantity}")

    report.append("\n" + "=" * 50)
    report.append("VALIDATION COMPLETED")
    report.append("=" * 50)

    with open(REPORT_FILE, "w") as file:

        for line in report:
            file.write(line + "\n")

    print("\n".join(report))

    print(f"\nReport Saved : {REPORT_FILE}")


# ============================================
# Main
# ============================================

def main():

    validate()


if __name__ == "__main__":
    main()