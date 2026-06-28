import pandas as pd
import random

# Number of products to generate
NUM_PRODUCTS = 1000

# Categories with brands and products
CATEGORIES = {
    "Electronics": {
        "brands": ["Dell", "HP", "Lenovo", "Apple", "Samsung", "Sony"],
        "products": [
            "Laptop", "Smartphone", "Monitor", "Keyboard",
            "Mouse", "Tablet", "Smart Watch", "Printer"
        ],
        "price_range": (5000, 150000)
    },

    "Fashion": {
        "brands": ["Nike", "Adidas", "Puma", "Levis", "Zara"],
        "products": [
            "T-Shirt", "Jeans", "Shoes", "Jacket", "Cap"
        ],
        "price_range": (300, 8000)
    },

    "Home & Kitchen": {
        "brands": ["Prestige", "Philips", "Bajaj"],
        "products": [
            "Mixer", "Cookware", "Vacuum Cleaner",
            "Bottle", "Dining Table"
        ],
        "price_range": (500, 20000)
    },

    "Books": {
        "brands": ["Pearson", "O'Reilly", "McGraw Hill"],
        "products": [
            "Python Programming",
            "SQL Essentials",
            "Machine Learning",
            "Data Science"
        ],
        "price_range": (200, 2500)
    },

    "Sports": {
        "brands": ["SG", "Nivia", "Yonex"],
        "products": [
            "Football", "Cricket Bat", "Yoga Mat", "Dumbbells"
        ],
        "price_range": (500, 15000)
    }
}


def generate_products():
    products = []

    for product_id in range(1, NUM_PRODUCTS + 1):

        category = random.choice(list(CATEGORIES.keys()))

        brand = random.choice(CATEGORIES[category]["brands"])

        product_name = random.choice(CATEGORIES[category]["products"])

        min_price, max_price = CATEGORIES[category]["price_range"]

        price = round(random.uniform(min_price, max_price), 2)

        stock = random.randint(20, 500)

        products.append({
            "product_id": product_id,
            "product_name": f"{brand} {product_name}",
            "category": category,
            "brand": brand,
            "price": price,
            "stock": stock
        })

    return pd.DataFrame(products)


def main():

    df = generate_products()

    df.to_csv("data/raw/products.csv", index=False)

    print(f"✅ {len(df)} products generated successfully.")


if __name__ == "__main__":
    main()