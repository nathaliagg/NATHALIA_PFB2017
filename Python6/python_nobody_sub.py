#!usr/bin/env python3
import re

#sub nobody for my name

nobody_file = open("Python_06_nobody.txt","r")
text_nobody = nobody_file.readlines()

# if re.search(r"Nobody",text_nobody):
#	print("Is there 'Nobody in the text'?")

# text_a = re.findall(r"Nobody",text_nobody)
# print("Yes! I found", len(text_a), "'Noboby' in the text")

for line in text_nobody:
	change = re.sub(r"Nobody", "Nathalia", line)
	print(change)
	change = open("Python_06_nobody-Nathalia.out", "w")
	
