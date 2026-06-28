import os
import pandas as pd
import re

# ============================================
# Create cleaned folder
# ============================================

os.makedirs("data/cleaned", exist_ok=True)


# ============================================
# Email Validation
# ============================================

def valid_email(email):

    if pd.isna(email):
        return False

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return bool(re.match(pattern, str(email)))


# ============================================
# Phone Validation
# ============================================

def valid_phone(phone):

    phone = str(phone)

    return phone.isdigit() and len(phone) == 10


# ============================================
# Cleaning Function
# ============================================

def clean_customers():

    print("Loading Dirty Customer Dataset...")

    df = pd.read_csv("data/dirty/customers.csv")

    original_rows = len(df)

    # -----------------------------------
    # Remove duplicate customer IDs
    # -----------------------------------

    df.drop_duplicates(
        subset="customer_id",
        inplace=True
    )

    # -----------------------------------
    # Remove duplicate emails
    # -----------------------------------

    df.drop_duplicates(
        subset="email",
        keep="first",
        inplace=True
    )

    # -----------------------------------
    # Remove blank names
    # -----------------------------------

    df["first_name"] = df["first_name"].fillna("").str.strip()

    df = df[df["first_name"] != ""]

    # -----------------------------------
    # Remove missing emails
    # -----------------------------------

    df = df[df["email"].notna()]

    # -----------------------------------
    # Keep only valid emails
    # -----------------------------------

    df = df[df["email"].apply(valid_email)]

    # -----------------------------------
    # Keep only valid phone numbers
    # -----------------------------------

    df["phone"] = df["phone"].astype(str)

    df = df[df["phone"].apply(valid_phone)]

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
        "data/cleaned/customers.csv",
        index=False
    )

    # -----------------------------------
    # Report
    # -----------------------------------

    cleaned_rows = len(df)

    removed = original_rows - cleaned_rows

    print("\n========== Customer Cleaning Report ==========")

    print(f"Original Records : {original_rows}")

    print(f"Clean Records    : {cleaned_rows}")

    print(f"Removed Records  : {removed}")

    print("Saved to data/cleaned/customers.csv")

    print("==============================================")


# ============================================
# Main
# ============================================

def main():

    clean_customers()


if __name__ == "__main__":
    main()