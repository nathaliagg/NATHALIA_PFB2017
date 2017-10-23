#!/usr/bin/env python3

#source of the code was: biostars, by Manu Prestat.
#extract fasta sequence from a file
#using ids from a text file

import string
import sys

ListofIDs = sys.argv[1]
fastafile = sys.argv[2]

try:
	ids=open((ListofIDs), 'r')
except IOError:
	print("File error:", ListofIDs)

lignes = ids.readlines()
req =[]
for linge in lignes:
	req.append(linge.strip())

#reading the fasta file to cut
handle = open(fastafile)

bank = {}
seqIDmap = {}
seq_id = handle.next()

while (seq_id[0]!=">"):
	seq_id = handle.next()
while True:
	try:
		seq = handle.next()
		line = handle.next()
		while (line[0]!=">"):
			seq = seq+line
			line = handle.next()
		bank[seq_id]=seq
		IDclean=string.split(seq_id, "")[0][1:].strip()
		seqIDmap[IDclean]=seq_id
		seq_id = line #for the next
	except StopIteration:
		break
#last line
bank[seq_id]=seq
seqIDmap[string.split(seq_id, "")[0][1:].strip()]=seq_id

handle.close()

###end reading the potentially big fasta file

faName =fastafile.split("/")[-1]
listName=ListofIDs.split("/")[-1]
subsetName=listName+"-"+faName
subset= open(subsetName, 'w')
nbNF=0

for i in req:
	try:
		subset.write(seqIDmap[i].strip()+"\n")
		subset.write(bank[seqIDmap[i]].strip()+"\n")
	except KeyError:
		print(i, "Not found in fasta")
		nbNF+=1

subset.close()

print(nbNF, "IDs (listed above) from", listName, "have not been found in", faName)
print("the subset fasta file", subsetName, "is now created")

 
