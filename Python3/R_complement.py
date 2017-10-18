#!/usr/bin/env python3
import sys

# This is a script that returns both the complement and
# the reverse complement of a DNA sequence.

# sys.argv[0] is the name of the script

dna=str(sys.argv[1])

dna_a = dna.replace('A','t')
dna_t = dna_a.replace('T','a')
dna_c = dna_t.replace('C','g')
dna_g = dna_c.replace('G','c')
complement_dna = dna_g.upper()
reverse_complement = complement_dna[::-1]

original_answer = "5' {0} 3'".format(dna) 
a = "Original Sequence"

complement_answer = "3' {0} 5'".format(complement_dna)
b = "Complement sequence"

reverse_answer = "5' {0} 3'".format(reverse_complement)
c = "Reverse sequence"

print("{0:<20} {1}".format(a,original_answer))
print("{0:<20} {1}".format(b,complement_answer)) 
print("{0:<20} {1}".format(c,reverse_answer)) 
