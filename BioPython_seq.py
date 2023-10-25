#!/usr/bin/env python3
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


sequence = Seq("aaaatgggggggggggccccgtt")
# Create a Sequence record using SeqRecord
record = SeqRecord(sequence, id="12345", description="example1", annotations={"molecule_type": "DNA"})
# Write the Sequence record to BioPython_seq.gb file using SeqIO.write in genbank format
SeqIO.write(record, "BioPython_seq.gb", "genbank")

