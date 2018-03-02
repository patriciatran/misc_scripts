## From a fasta file with sequences of various lengths, this scripts get all sequences for which the length is above a certain cutoff (greater or equal to)

## Usage:
# python2.7 Fasta_parser [fasta file to parse] [cutoff] [output file name]

## Depends on BioPython (https://github.com/biopython/biopython.github.io/)

from Bio import SeqIO
import sys

#Input

fasta_input = open(str(sys.argv[1]),"rU")
# The cut_off must be a positive integer
cut_off = int(sys.argv[2])

#Output
output_fasta = open(str(sys.argv[3]),"w")

long_sequences=[] #set up an empty list
for record in SeqIO.parse (fasta_input, "fasta"):
	if len(record.seq) >= cut_off :
	# Add this record to list
		long_sequences.append(record)

print("Found %i sequences longer than" + cutoff % len(long_sequences))

#print(long_sequences)
SeqIO.write(long_sequences, output_fasta, "fasta")
output_fasta.close()
