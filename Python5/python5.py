#!usr/bin/env python3

# file name is 'Python_05.txt'

#open the same file with different access modes one at a time
#name each open function differently

file_read = open("Python_05.txt", "r")
file_write = open("Python_05.out", "w") #will direct the output to the file named Python_05.out
#don't name read and write files the same!

#don't create a variable to store the contents of the file
#because it will read as a string! And each letter will be in one line...
#you don't want each character in one line!

#loop to change uppercase each line
for line in file_read:
	line = line.rstrip() # removes \n
	line = line.upper() # uppercase letters
	print(line) # now the file contain real text

#close file
file_read.close()
file_write.close()
