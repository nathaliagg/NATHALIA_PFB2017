#!/usr/bin/env python3

import sys

DNA=str(sys.argv[1])

if 'AGGT' in DNA:
	print ("found AGGT in your DNA sequence")

elif 'U' in DNA:
	print ("OPS! I found U. I think this is RNA sequence")

elif 'R' in DNA:
	print ("OPS! I found R. This might be a PROTEIN sequence")

elif 'K' in DNA:
	print ("OPS! I found K. This might be a PROTEIN sequence")

else:
	print ("did not found AGGT in your DNA sequence")
