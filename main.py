from src.cli.reports import *

while True:

    print("\n========================================")
    print("   E-Commerce Analytics Dashboard")
    print("========================================")

    print("1. Database Summary")
    print("2. Top Customers")
    print("3. Monthly Revenue")
    print("4. Revenue by Category")
    print("5. Top Selling Products")
    print("6. Customer Purchase Frequency")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        database_summary()

    elif choice == "2":

        top_customers()

    elif choice == "3":

        monthly_revenue()

    elif choice == "4":

        revenue_by_category()

    elif choice == "5":

        top_products()

    elif choice == "6":

        purchase_frequency()

    elif choice == "7":

        print("\nThank You for Using E-Commerce Analytics System.")

        break

    else:

        print("\nInvalid Choice!")