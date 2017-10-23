#!usr/bin/env python3
import sys

dict_fasta = {}

with open(sys.argv[1], 'r') as read_fasta_file:
	for line in read_fasta_file:
		line = line.rstrip()
		if line.startswith('>'):
			active_line = line[1:]
			if active_line not in dict_fasta:
				dict_fasta[active_line] = ''
		else:
			dict_fasta[active_line] = dict_fasta[active_line] + line

print(dict_fasta)



