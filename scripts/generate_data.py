import os
import csv
import random
import numpy as np

# --- config ---
OUTPUT_CSV = "../data/raw.csv"
COMPANIES = ["MyCompany", "Company A", "Company B", "Company C", "Company D", "Company E", "Company F", "Company G", "Company H", "Company I", "Company J", "Company K", "Company L", "Company M", "Company N", "Company O", "Company P", "Company Q", "Company R", "Company S", "Company T", "Company U", "Company V", "Company W", "Company X", "Company Y", "Company Z"]
SEED = 42  # for reproducibility

# --- ensure folder exists ---
os.makedirs("../data", exist_ok=True)

# --- simulation ---
def simulate_company_data(n):
    random.seed(SEED)
    np.random.seed(SEED)

    data = []
    for _ in range(n):
        product_count = random.randint(20, 100)
        global_presence = random.choices(["Low", "Medium", "High"], weights=[0.29, 0.42, 0.29])[0]
        nps_score = int(np.clip(np.random.normal(20, 40), -100, 100))
        avg_price = round(random.uniform(150, 450), 2)
        brand_buzz = random.choices(["Low", "Medium", "High"], weights=[0.29, 0.42, 0.29])[0]
        cx_rating = round(random.uniform(3.0, 5.0), 1)
        revenue = int(np.clip(np.random.normal(600, 300), 100, 2000))

        data.append([
            product_count,
            global_presence,
            nps_score,
            avg_price,
            brand_buzz,
            cx_rating,
            revenue
        ])
    return data

# --- populate csv ---
with open(OUTPUT_CSV, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Company", "Product Count", "Global Presence", "NPS Score", "Avg Price", "Brand Buzz", "CX Rating", "Revenue ($M)"])
    simulated = simulate_company_data(len(COMPANIES))
    for i in range(len(COMPANIES)):
        writer.writerow([COMPANIES[i]] + simulated[i])

print(f"raw data saved to {OUTPUT_CSV}")
