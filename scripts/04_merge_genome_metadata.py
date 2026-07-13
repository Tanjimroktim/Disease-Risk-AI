import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Load extracted genome features
features = pd.read_csv(BASE_DIR / "data" / "processed" / "genome_features.csv")

# Load metadata
metadata = pd.read_csv(
    BASE_DIR / "data" / "genome" / "sequences.tsv",
    sep="\t"
)

# Keep only useful columns
metadata = metadata[
    [
        "Accession",
        "Pangolin",
        "Genotype",
        "Country",
        "Geo_Location",
        "Collection_Date",
        "Host"
    ]
]

# Remove version number (.1) from genome feature accession
features["Accession"] = features["Accession"].str.split(".").str[0]

# Merge
merged = pd.merge(features, metadata, on="Accession", how="left")

print("="*50)
print("Merged Dataset")
print("="*50)

print(merged.head())

print("\nShape:", merged.shape)

# Save
output = BASE_DIR / "data" / "processed" / "genome_master.csv"

merged.to_csv(output, index=False)

print("\nSaved Successfully:")
print(output)