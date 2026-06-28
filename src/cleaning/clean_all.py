from clean_customers import clean_customers
from clean_products import clean_products
from clean_orders import clean_orders
from clean_order_items import clean_order_items
from clean_payments import clean_payments


def main():

    print("\n========== STARTING DATA CLEANING ==========\n")

    clean_customers()
    clean_products()
    clean_orders()
    clean_order_items()
    clean_payments()

    print("\n===========================================")
    print("✅ ALL DATASETS CLEANED SUCCESSFULLY")
    print("📁 Clean files saved in data/cleaned/")
    print("===========================================\n")


if __name__ == "__main__":
    main()