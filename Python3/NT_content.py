#!/usr/bin/env python3
import sys

# This is a script that calculates the AT and GC content of a DNA sequence.
#sys.argv[0] is the name of the script

DNA=str(sys.argv[1])

DNA_A = DNA.count("A")
DNA_T = DNA.count("T")
DNA_C = DNA.count("C")
DNA_G = DNA.count("G")

AT_content = (DNA_A+DNA_T)/len(DNA)
GC_content = (DNA_C+DNA_G)/len(DNA)
AT="{:.1%}".format(AT_content)
GC="{:.1%}".format(GC_content)

phrase= "Your sequence has {} AT content, and {} GC content."
print(phrase.format(AT,GC))
