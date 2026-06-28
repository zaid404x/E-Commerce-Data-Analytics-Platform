import pandas as pd
import random
from faker import Faker

# Initialize Faker for Indian data
fake = Faker("en_IN")

# Number of customers
NUM_CUSTOMERS = 10000

# List to store customer data
customers = []

# Generate customer records
for customer_id in range(1, NUM_CUSTOMERS + 1):

    customer = {
        "customer_id": customer_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "gender": random.choice(["Male", "Female"]),
        "city": fake.city(),
        "state": fake.state(),
        "signup_date": fake.date_between(start_date="-3y", end_date="today")
    }

    customers.append(customer)

# Convert list to DataFrame
df = pd.DataFrame(customers)

# Save CSV
df.to_csv("data/raw/customers.csv", index=False)

print(f"✅ Successfully generated {NUM_CUSTOMERS} customer records.")