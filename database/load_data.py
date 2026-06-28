import sqlite3
import pandas as pd
import os

# ============================================
# Configuration
# ============================================

DB_PATH = "database/ecommerce.db"
SCHEMA_PATH = "database/schema.sql"

TABLE_LOAD_ORDER = [
    ("Customers", "data/validated/customers.csv"),
    ("Products", "data/validated/products.csv"),
    ("Orders", "data/validated/orders.csv"),
    ("Order_Items", "data/validated/order_items.csv")
]


# ============================================
# Create Database
# ============================================

def create_database():

    print("Creating SQLite Database...")

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    with open(SCHEMA_PATH, "r") as file:

        cursor.executescript(file.read())

    connection.commit()

    print("✅ Database Created Successfully.")

    return connection


# ============================================
# Load CSV
# ============================================

def load_csv(connection, table_name, csv_path):

    print(f"\nLoading {table_name}...")

    df = pd.read_csv(csv_path)

    try:

        df.to_sql(
            table_name,
            connection,
            if_exists="append",
            index=False
        )

        print(f"✅ Loaded {len(df)} records.")

    except Exception as e:

        print(f"\n❌ Failed while loading {table_name}")

        print(e)

        raise


# ============================================
# Verify
# ============================================

def verify_database(connection):

    cursor = connection.cursor()

    print("\n========== DATABASE SUMMARY ==========\n")

    for table, _ in TABLE_LOAD_ORDER:

        cursor.execute(f"SELECT COUNT(*) FROM {table}")

        count = cursor.fetchone()[0]

        print(f"{table:<15} : {count}")

    print("\n======================================\n")


# ============================================
# Main
# ============================================

def main():

    if os.path.exists(DB_PATH):

        os.remove(DB_PATH)

        print("Old database removed.")

    connection = create_database()

    for table, path in TABLE_LOAD_ORDER:

        load_csv(connection, table, path)

    verify_database(connection)

    connection.commit()

    connection.close()

    print("✅ Database Loaded Successfully.")
    print("📁 database/ecommerce.db")


if __name__ == "__main__":

    main()