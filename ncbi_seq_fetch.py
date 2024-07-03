from Bio import Entrez, SeqIO

# Function to fetch nucleotide sequences from NCBI
def fetch_nucleotide_sequences(genbank_ids):
    # Fetch sequences
    try:
        # Use Entrez.efetch to fetch data from NCBI
        with Entrez.efetch(db="nucleotide", id=genbank_ids, rettype="gb", retmode="text") as handle:
            # Parse the sequences
            sequences = list(SeqIO.parse(handle, "genbank"))
            return sequences
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# List of GenBank IDs (replace with your desired IDs)
genbank_ids = ["NM_001301717", "NM_001301718"]

# Fetch the sequences
sequences = fetch_nucleotide_sequences(genbank_ids)

# Save the fetched sequences to a text file
if sequences:
    with open("nucleotide_sequences.txt", "w") as output_file:
        for seq_record in sequences:
            output_file.write(f"ID: {seq_record.id}\n")
            output_file.write(f"Name: {seq_record.name}\n")
            output_file.write(f"Description: {seq_record.description}\n")
            output_file.write(f"Sequence length: {len(seq_record)}\n")
            output_file.write(f"Sequence: {seq_record.seq}\n\n")
    print("Sequences saved to nucleotide_sequences.txt")
else:
    print("No sequences fetched.")
