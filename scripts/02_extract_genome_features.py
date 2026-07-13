from Bio import SeqIO
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

fasta_file = BASE_DIR / "data" / "genome" / "sequences.fasta"

records = list(SeqIO.parse(str(fasta_file), "fasta"))

features = []

for record in records:

    sequence = str(record.seq).upper()

    length = len(sequence)

    gc = ((sequence.count("G") + sequence.count("C")) / length) * 100

    n_count = sequence.count("N")

    features.append({
        "Accession": record.id,
        "Length": length,
        "GC_Content": round(gc, 2),
        "N_Count": n_count
    })

df = pd.DataFrame(features)

print(df.head())

output = BASE_DIR / "data" / "processed" / "genome_features.csv"

df.to_csv(output, index=False)

print("\nSaved to:")
print(output)