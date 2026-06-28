import os
import pandas as pd

# ============================================
# Create cleaned folder
# ============================================

os.makedirs("data/cleaned", exist_ok=True)


# ============================================
# Correct Category Names
# ============================================

CATEGORY_MAPPING = {
    "Electroncs": "Electronics",
    "Fashon": "Fashion",
    "Sportz": "Sports"
}


# ============================================
# Cleaning Function
# ============================================

def clean_products():

    print("Loading Dirty Product Dataset...")

    df = pd.read_csv("data/dirty/products.csv")

    original_rows = len(df)

    # -----------------------------------
    # Remove Duplicate Product IDs
    # -----------------------------------

    df.drop_duplicates(
        subset="product_id",
        keep="first",
        inplace=True
    )

    # -----------------------------------
    # Remove Duplicate Product Names
    # -----------------------------------

    df.drop_duplicates(
        subset="product_name",
        keep="first",
        inplace=True
    )

    # -----------------------------------
    # Fix Wrong Category Names
    # -----------------------------------

    df["category"] = df["category"].replace(CATEGORY_MAPPING)

    # -----------------------------------
    # Convert Negative Prices to Positive
    # -----------------------------------

    df["price"] = df["price"].abs()

    # -----------------------------------
    # Replace Zero Stock with Random Stock
    # -----------------------------------

    df.loc[df["stock"] <= 0, "stock"] = 50

    # -----------------------------------
    # Remove Rows with Missing Values
    # -----------------------------------

    df.dropna(inplace=True)

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
        "data/cleaned/products.csv",
        index=False
    )

    cleaned_rows = len(df)

    removed = original_rows - cleaned_rows

    print("\n========== Product Cleaning Report ==========")

    print(f"Original Records : {original_rows}")

    print(f"Clean Records    : {cleaned_rows}")

    print(f"Removed Records  : {removed}")

    print("Saved to data/cleaned/products.csv")

    print("=============================================")


# ============================================
# Main
# ============================================

def main():

    clean_products()


if __name__ == "__main__":
    main()