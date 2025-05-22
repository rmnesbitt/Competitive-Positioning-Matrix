import pandas as pd

# --- load data ---
input_path = "../data/normalization.csv"
df = pd.read_csv(input_path)

# --- produce dimensions ---
df['Market Reach'] = (
    0.1 * df['Product Count Normal'] +
    0.2 * df['Global Presence Normal'] +
    0.4 * df['Revenue Normal'] +
    0.3 * df['Price Access Normal']
)

df['Perceived Value'] = (
    0.4 * df['NPS Score Normal'] +
    0.2 * df['Brand Buzz Normal'] +
    0.4 * df['CX Rating Normal']
)

df['Market Reach'] = df['Market Reach'].round(4)
df['Perceived Value'] = df['Perceived Value'].round(4)

# --- save csv ---
df.to_csv("../data/dimensions.csv", index=False)

print("saved dimensions to ../data/dimensions.csv")
