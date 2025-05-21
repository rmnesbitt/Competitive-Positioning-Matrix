import pandas as pd
import numpy as np
import os

# --- load raw data ---
input_path = "../data/features.csv"
df = pd.read_csv(input_path)

# --- normalization ---
df['Revenue Normal'] = ((df['Revenue ($M)'] - df['Revenue ($M)'].min()) / (df['Revenue ($M)'].max() - df['Revenue ($M)'].min())).round(4)
df['Product Count Normal'] = ((df['Product Count'] - df['Product Count'].min()) / (df['Product Count'].max() - df['Product Count'].min())).round(4)
df['NPS Score Normal'] = ((df['NPS Score'] - df['NPS Score'].min()) / (df['NPS Score'].max() - df['NPS Score'].min())).round(4)
df['CX Rating Normal'] = ((df['CX Rating'] - df['CX Rating'].min()) / (df['CX Rating'].max() - df['CX Rating'].min())).round(4)
df['Price Access Normal'] = ((df['Price Accessibility'] - df['Price Accessibility'].min()) / (df['Price Accessibility'].max() - df['Price Accessibility'].min())).round(4)
df['Global Presence Normal'] = ((df['Global Presence Num'] - df['Global Presence Num'].min()) / (df['Global Presence Num'].max() - df['Global Presence Num'].min())).round(4)
df['Brand Buzz Normal'] = ((df['Brand Buzz Num'] - df['Brand Buzz Num'].min()) / (df['Brand Buzz Num'].max() - df['Brand Buzz Num'].min())).round(4)

# --- save norm values to csv ---
os.makedirs("../data", exist_ok=True)
df.to_csv("../data/normalization.csv", index=False)

print("normalized and saved to ../data/normalization.csv")