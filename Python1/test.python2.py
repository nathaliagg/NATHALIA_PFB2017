#!/usr/bin/env python3
import sys

#in the command-line type this: python3 test.python2.py Nathalia Brazil green sports dog Noel corgi
#the names that will fill out the spaces of variables (sys.argv[1 to 7]) should be in order
#sys.argv[0] is the name of the script

name=str(sys.argv[1])
origin=str(sys.argv[2])
color=str(sys.argv[3])
activity=str(sys.argv[4])
animal=str(sys.argv[5])
dog_name=str(sys.argv[6])
breed=str(sys.argv[7])

print("My name is", name, ".", "I'm from", origin,".", "My favorite color is", color, ".", "I love practicing",\
activity, "with my friends.", "My favorite animal is my", animal,",", dog_name, ".", "My", animal, dog_name,\
"is a", breed, ".")
