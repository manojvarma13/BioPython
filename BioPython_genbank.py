#!/usr/bin/env python3

from Bio import SeqIO
from Bio import Entrez

Entrez.email = "tekumalla.sa@husky.neu.edu"
r_seq = []
# Create a list to contain the retrieved sequences generated later
# Generate SeqIO objects using the code below
with Entrez.efetch (
     db = "nucleotide", rettype = "gb",retmode = "text", id = "515056"
     ) as handle:
          seq_record_1 = SeqIO.read(handle,"gb")
with Entrez.efetch(
     db = "nucleotide",rettype = "gb", retmode = "text", id = "J01673.1"
     ) as handle:
          seq_record_2 = SeqIO.read(handle,"gb")
r_seq = [seq_record_1, seq_record_2]
print(seq_record_1.seq, seq_record_2.seq)
print(seq_record_1.features, seq_record_2.features)
# Use .features attributes to populate type, location and strand attributes.
