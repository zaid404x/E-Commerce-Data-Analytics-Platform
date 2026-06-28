# 🛒 E-Commerce Data Analytics Platform

## 📌 Project Overview

The **E-Commerce Data Analytics Platform** is an end-to-end data engineering and analytics project developed using **Python, Pandas, SQLite, and SQL**. The project simulates a real-world e-commerce environment by generating synthetic datasets, introducing intentional data quality issues, cleaning and validating the data, loading it into a relational database, and performing advanced SQL analytics to derive business insights.

The system follows a complete ETL (Extract, Transform, Load) pipeline and includes a command-line reporting tool for interactive business reporting.

---

# 🚀 Features

* Synthetic e-commerce dataset generation using Python
* Intentional dirty data generation for testing
* Data cleaning using Pandas
* Data validation and referential integrity checks
* SQLite relational database implementation
* Advanced SQL analytics
* Business insight generation
* Interactive command-line reporting dashboard
* Modular and scalable project structure

---

# 🏗️ Project Workflow

```text
Data Generation
        │
        ▼
Dirty Data Generation
        │
        ▼
Data Cleaning
        │
        ▼
Data Validation
        │
        ▼
SQLite Database
        │
        ▼
Advanced SQL Analytics
        │
        ▼
Business Reports
        │
        ▼
Command Line Dashboard
```

---

# 📂 Project Structure

```text
E-Commerce Data Analytics Platform
│
├── data/
│   ├── raw/
│   ├── dirty/
│   ├── cleaned/
│   └── validated/
│
├── database/
│   ├── ecommerce.db
│   ├── schema.sql
│   ├── load_data.py
│   └── queries.sql
│
├── reports/
│   └── validation_report.txt
│
├── src/
│   ├── generator/
│   ├── cleaning/
│   ├── validation/
│   └── cli/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

* Python 3.x
* Pandas
* SQLite3
* SQL
* Faker
* Tabulate
* VS Code

---

# 📊 Dataset

The project generates realistic synthetic datasets for:

* Customers
* Products
* Orders
* Order Items

The generated data contains intentional inconsistencies including:

* Missing values
* Duplicate records
* Invalid emails
* Incorrect product prices
* Negative quantities
* Broken foreign-key references

These inconsistencies are later cleaned and validated during the ETL process.

---

# 🧹 ETL Pipeline

### Data Generation

Synthetic datasets are generated using Python and the Faker library.

### Dirty Data Generation

Intentional inconsistencies are introduced to simulate real-world data quality issues.

### Data Cleaning

Pandas is used to remove duplicates, fix invalid values, normalize data, and prepare datasets for analysis.

### Data Validation

Referential integrity, duplicate records, invalid emails, and data consistency are verified before loading into the database.

### Database Loading

The cleaned datasets are loaded into a SQLite database using Python.

---

# 🗄️ Database Schema

The SQLite database contains the following tables:

* Customers
* Products
* Orders
* Order_Items

Relationships are maintained using primary and foreign keys.

---

# 📈 SQL Analytics

The project includes SQL queries covering:

* Basic SQL Queries
* Aggregate Functions
* Joins
* Common Table Expressions (CTEs)
* Window Functions
* Ranking Functions
* Running Totals
* Customer Segmentation
* Revenue Analysis
* Product Performance Analysis
* Monthly Sales Trends

---

# 💻 Command Line Dashboard

The application provides an interactive CLI dashboard where users can:

* View database summary
* Display top customers
* Analyze monthly revenue
* View revenue by category
* Display top-selling products
* Analyze customer purchase frequency

---

# ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/zaid404x/ecommerce-data-analytics-platform.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Dataset

```bash
python src/generator/generate_customers.py
python src/generator/generate_products.py
python src/generator/generate_orders.py
python src/generator/generate_order_items.py
```

### Generate Dirty Data

```bash
python src/generator/introduce_dirty_data.py
```

### Clean Data

```bash
python src/cleaning/clean_all.py
```

### Validate Data

```bash
python src/validation/validate_data.py
```

### Load Database

```bash
python database/load_data.py
```

### Run Dashboard

```bash
python main.py
```

---

# 📷 Sample Output

The CLI dashboard provides interactive reports such as:

* Database Summary
* Revenue Reports
* Top Customers
* Top Products
* Monthly Revenue Trends
* Customer Purchase Frequency

---

# 🎯 Learning Outcomes

This project demonstrates practical implementation of:

* Data Engineering
* ETL Pipelines
* Data Cleaning
* Data Validation
* Relational Database Design
* Advanced SQL
* Business Analytics
* Python Programming
* Command-Line Application Development

---

# 👨‍💻 Author

**Zaid Pathan**

B.Tech Computer Science Engineering
DATA ENGINEER

---

