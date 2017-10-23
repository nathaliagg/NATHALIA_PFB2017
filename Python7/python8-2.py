#!usr/bin/env python3
import sys

#problem_2

#creates a function to display fasta sequence in lines of 60 nt long

def split_60(dna):
	dna_file = open(sys.argv[1], 'r')
	dna = dna_file.readlines()
	if len(dna)>60:
		for l in range(0,len(dna),60):
			print(dna[l:l+60]) 
			
		 	

for line in dna:
		line = line.rstrip()
		if len(line) > 60:
			for i in range(0,len(line),60)):
				print(i.join
			outfile.write('\n'.join(line[i:i+60] for i in xrange(0,len(line),60)))




#with open(sys.argv[1], 'r') as dna, open('python8-1-out.txt', 'w') as outfile:
#	for line in read_file:
#		line = line.rstrip()
#		if len(line) > 60:
#			outfile.write('\n'.join(line[i:i+60] for i in xrange(0,len(line),60))



	
