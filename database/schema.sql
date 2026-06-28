PRAGMA foreign_keys = ON;

-- ===========================
-- Customers
-- ===========================

CREATE TABLE IF NOT EXISTS Customers (

    customer_id INTEGER PRIMARY KEY,

    first_name TEXT NOT NULL,

    last_name TEXT NOT NULL,

    email TEXT UNIQUE,

    phone TEXT,

    gender TEXT,

    city TEXT,

    state TEXT,

    signup_date DATE
);

-- ===========================
-- Products
-- ===========================

CREATE TABLE IF NOT EXISTS Products (

    product_id INTEGER PRIMARY KEY,

    product_name TEXT,

    category TEXT,

    brand TEXT,

    price REAL,

    stock INTEGER
);

-- ===========================
-- Orders
-- ===========================

CREATE TABLE IF NOT EXISTS Orders (

    order_id INTEGER PRIMARY KEY,

    customer_id INTEGER,

    order_date DATE,

    order_status TEXT,

    total_amount REAL,

    FOREIGN KEY(customer_id)
        REFERENCES Customers(customer_id)
);

-- ===========================
-- Order Items
-- ===========================

CREATE TABLE IF NOT EXISTS Order_Items (

    order_item_id INTEGER PRIMARY KEY,

    order_id INTEGER,

    product_id INTEGER,

    quantity INTEGER,

    unit_price REAL,

    line_total REAL,

    FOREIGN KEY(order_id)
        REFERENCES Orders(order_id),

    FOREIGN KEY(product_id)
        REFERENCES Products(product_id)
);