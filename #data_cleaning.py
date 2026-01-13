
import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/netflix.csv")

# Drop null values
df_cleaned = df.dropna()

# Save cleaned data
df_cleaned.to_csv("data/processed/cleaned_netflix.csv", index=False)

print("Data cleaning completed")
