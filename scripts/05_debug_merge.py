import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

features = pd.read_csv(BASE_DIR / "data" / "processed" / "genome_features.csv")
metadata = pd.read_csv(BASE_DIR / "data" / "genome" / "sequences.tsv", sep="\t")

print("Feature Accession:")
print(features["Accession"].head())

print("\nMetadata Accession:")
print(metadata["Accession"].head())