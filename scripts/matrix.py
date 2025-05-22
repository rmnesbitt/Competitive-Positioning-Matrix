import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# --- load data ---
df = pd.read_csv("../data/dimensions.csv")

# --- ranks ---
df["Reach Rank"] = df["Market Reach"].rank(ascending=False).astype(int).round(2)
df["Value Rank"] = df["Perceived Value"].rank(ascending=False).astype(int).round(2)
df["Overall Rank"] = ((df["Reach Rank"]+df["Value Rank"]) / 2).rank().astype(int).round(2)

# --- save ranks ---
output_df = df[["Company", "Reach Rank", "Value Rank", "Overall Rank"]].sort_values(by="Overall Rank", ascending=False)
output_df.to_csv("../data/matrix.csv", index=False)

# --- matrix plot settings ---
plt.figure(figsize=(8, 6))
plt.axhline(0.5, color='gray', linestyle='--')  # horizontal midline
plt.axvline(0.5, color='gray', linestyle='--')  # vertical midline

# ---  matrix plot ---
for i, row in df.iterrows():
    plt.scatter(row["Market Reach"], row["Perceived Value"], s=100)
    label = row["Company"].replace("Company", "").strip()
    plt.text(row["Market Reach"] + 0.01, row["Perceived Value"] + 0.01, label, fontsize=9)

# --- matrix labels ---
plt.title("Competitive Positioning Matrix")
plt.xlabel("Market Reach (Quantity)")
plt.ylabel("Perceived Value (Quality)")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True, linestyle=':', alpha=0.5)

# --- save matrix ---
os.makedirs("../output/charts", exist_ok=True)
plt.tight_layout()
plt.savefig("../output/charts/matrix.png")
plt.close()

# --- bars sort ---
df_sorted = df.sort_values("Overall Rank")

# --- bar stacks ---
companies = df_sorted["Company"]
reach_ranks = df_sorted["Reach Rank"]
value_ranks = df_sorted["Value Rank"]

# --- bars plot ---
plt.figure(figsize=(10, 6))
bar1 = plt.barh(companies, reach_ranks, label="Reach Rank", color="#4caf50")
bar2 = plt.barh(companies, value_ranks, left=reach_ranks, label="Value Rank", color="#2196f3")

# --- bars labels
plt.xlabel("Cumulative Rank (Lower = Better)")
plt.title("Stacked Rank Breakdown by Company")
plt.gca().invert_yaxis()  # Best on top
plt.legend()

for i in range(len(companies)):
    total = reach_ranks.iloc[i] + value_ranks.iloc[i]
    plt.text(total + 0.2, i, f"Total: {total:.0f}", va='center', fontsize=9)

# --- save bars ---
os.makedirs("../output/charts", exist_ok=True)
plt.tight_layout()
plt.savefig("../output/charts/ranks.png")
plt.close()

print("matrix chart saved to ../data/matrix.csv")
print("ranks table saved to ../output/charts/ranks.png")
print("ranks chart saved to ../output/charts/ranks.png")