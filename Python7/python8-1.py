#!usr/bin/env python3
import sys

#problem_1

#creates an output file with fasta sequence in lines of 60 nt long

with open(sys.argv[1], 'r') as read_file, open('python8-1-out.txt', 'w') as outfile:
	for line in read_file:
		line = line.rstrip()
		if len(line) > 60:
			outfile.write('\n'.join(line[i:i+60] for i in xrange(0,len(line),60))



	
