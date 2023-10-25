#!/usr/bin/env python3

import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
# give positions for arguments(input, output file)
input_arg = sys.argv[1]
output_arg = sys.argv[2]
with open(output_arg, 'w') as handle:
    for rec in SeqIO.parse(input_arg, 'fasta'):
        #initiate for loop to parse the input file if the format is specified as fasta.
        handle.write(SeqRecord(id=rec.id, seq=rec.seq.reverse_complement()).format('fasta'))
        #write the output file in fasta format.
