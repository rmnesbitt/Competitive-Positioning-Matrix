import pandas as pd
import numpy as np
import os

# --- load raw data ---
input_path = "../data/raw.csv"
df = pd.read_csv(input_path)

# --- map features ---
ordinal_map = {"Low": 1, "Medium": 2, "High": 3}
df["Global Presence Num"] = df["Global Presence"].map(ordinal_map)
df["Brand Buzz Num"] = df["Brand Buzz"].map(ordinal_map)

# -- engineer features --
ideal_price = df['Avg Price'].mean()
std_dev = df['Avg Price'].std()
df['Price Accessibility'] = np.exp(-((df['Avg Price'] - ideal_price) ** 2) / (2 * std_dev ** 2)).round(4)

# --- save features to csv ---
os.makedirs("../data", exist_ok=True)
df.to_csv("../data/features.csv", index=False)

print("features mapped and saved to ../data/features.csv")
