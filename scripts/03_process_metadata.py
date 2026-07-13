import pandas as pd
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Metadata file
metadata_file = BASE_DIR / "data" / "genome" / "sequences.tsv"

# Load metadata
df = pd.read_csv(metadata_file, sep="\t")

print("=" * 50)
print("Metadata Overview")
print("=" * 50)

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# Save column names for inspection
columns_df = pd.DataFrame({"Column_Name": df.columns})
columns_df.to_csv(BASE_DIR / "data" / "processed" / "metadata_columns.csv", index=False)

print("\nColumn list saved successfully!")