import sqlite3

DB_PATH = "database/ecommerce.db"


def execute_query(query):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def database_summary():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    tables = [
        "Customers",
        "Products",
        "Orders",
        "Order_Items"
    ]

    print("\n========== DATABASE SUMMARY ==========\n")

    for table in tables:

        cursor.execute(f"SELECT COUNT(*) FROM {table}")

        count = cursor.fetchone()[0]

        print(f"{table:<15}: {count}")

    conn.close()


def top_customers():

    query = """

    SELECT
        c.customer_id,
        c.first_name || ' ' || c.last_name AS Customer,
        ROUND(SUM(o.total_amount),2) AS Revenue

    FROM Customers c

    JOIN Orders o

    ON c.customer_id=o.customer_id

    GROUP BY c.customer_id

    ORDER BY Revenue DESC

    LIMIT 10;

    """

    execute_query(query)


def monthly_revenue():

    query = """

    SELECT

        SUBSTR(order_date,1,7) AS Month,

        ROUND(SUM(total_amount),2) AS Revenue

    FROM Orders

    GROUP BY SUBSTR(order_date,1,7)

    ORDER BY Month;

    """

    execute_query(query)


def revenue_by_category():

    query = """

    SELECT

        p.category,

        ROUND(SUM(oi.line_total),2) AS Revenue

    FROM Products p

    JOIN Order_Items oi

    ON p.product_id=oi.product_id

    GROUP BY p.category

    ORDER BY Revenue DESC;

    """

    execute_query(query)


def top_products():

    query = """

    SELECT

        p.product_name,

        SUM(oi.quantity) AS Quantity

    FROM Products p

    JOIN Order_Items oi

    ON p.product_id=oi.product_id

    GROUP BY p.product_name

    ORDER BY Quantity DESC

    LIMIT 10;

    """

    execute_query(query)


def purchase_frequency():

    query = """

    SELECT

        customer_id,

        COUNT(order_id) AS Orders

    FROM Orders

    GROUP BY customer_id

    ORDER BY Orders DESC;

    """

    execute_query(query)