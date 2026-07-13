from Bio import SeqIO
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
fasta_file = BASE_DIR / "data" / "genome" / "sequences.fasta"

print("Reading:", fasta_file)

try:
    records = list(SeqIO.parse(str(fasta_file), "fasta"))

    print("=" * 50)
    print("Genome Analysis Report")
    print("=" * 50)
    print(f"Total Genome Sequences: {len(records)}")

    for i, record in enumerate(records[:5], start=1):
        print(f"\nGenome {i}")
        print(f"ID     : {record.id}")
        print(f"Length : {len(record.seq)} bp")

except Exception as e:
    print("\nERROR:")
    print(type(e).__name__)
    print(e)