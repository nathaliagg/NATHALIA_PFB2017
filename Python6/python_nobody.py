#!usr/bin/env python3
import re

#find the occurence of nobody, print out the position and which lines

nobody_file = open("Python_06_nobody.txt","r")
text_nobody = nobody_file.readlines()

print(text_nobody)

# if re.search(r"Nobody",text_nobody):
#	print("Is there 'Nobody in the text'?")

# text_a = re.findall(r"Nobody",text_nobody)
# print("Yes! I found", len(text_a), "'Nobody' in the text")

for line in text_nobody:
	
	for match in re.finditer(r"Nobody",line):
		whole = match.group(0)
		up = match.group(0)
		down = match.group(0)
		up_start = match.start(0)   # need to convert from 0 to 1 notation 
		up_end = match.end(0)
		dn_start = match.start(0)
		dn_end = match.end(0)

		output = [ whole , up, str(up_start), str(up_end) , down , str(dn_start) , str(dn_end)  ]

		print( "\t".join(output) )
