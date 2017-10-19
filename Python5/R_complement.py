#!/usr/bin/env python3
import sys

# This is a script that returns both the reverse complement of 
# DNA sequences in a file.

fasta = {}

with open(sys.argv[1]) as file_one:
	for line in file_one:
		line = line.rstrip()
		if len(line) == 0:
			continue
		if line.startswith(">"):
			active_sequence_name = line[1:]
			if active_sequence_name not in fasta:
				fasta[active_sequence_name] = ''
		else:
			fasta[active_sequence_name] = fasta[active_sequence_name]+line

print("This is the sequences in a dictionary")
print(fasta)

for key in fasta.items():
	sequence = fasta[key]	
	sequence = sequence.replace('A','t')
	sequence = sequence.replace('T','a')
	sequence = sequence.replace('C','g')
	sequence = sequence.replace('G','c')
	sequence = sequence.upper()
	sequence = sequence[::-1]
	
print(sequence)

#for key,value in fasta:
	#fasta[key] = fasta[key]+"  This is reverse complement  "+sequence


