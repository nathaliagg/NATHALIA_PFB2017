#!/usr/bin/env python3
import sys

# This script calculates the first and last nucleotides of each fragment 

# sys.argv[0] is the name of the script

dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG"

#
# EcoRI recognized GAATTC and cuts between G and A
# Retrieves how many sites in the given sequence
print ('EcoRI cuts between G and A nucleotides')
restriction_sites = dna.count('GAATTC')
print ('This DNA sequence has {} restriction sites'.format(restriction_sites))

#
#Position EcoRI recognizes it
position = dna.find('GAATTC')

#
#Position EcoRI cuts it
restrictionsite = position+1

#
#Extracting fragments
left_fragment = dna[0:restrictionsite]
right_fragment = dna[restrictionsite:]

#
#Getting the lengths of each fragment
len_left=len(left_fragment)
len_right=len(right_fragment)

#
# String formatting to print the info about these restriction fragments
print("Fragment\tPosition\tLength")
string_fragment_left = "Restriction site {} Fragment {} Length {}"
print(string_fragment_left.format(position,left_fragment,len_left))
string_fragment_right = "Restriction site {} Fragment {} Length {}"
print(string_fragment_right.format(restrictionsite,right_fragment,len_right))

#
#Create list with fragments
fragment_list=[]
fragment_list.append(left_fragment)
fragment_list.append(right_fragment)

#
#Sort the list
fragment_list.sort()
print(fragment_list)

#
#Sort by lenght
fragment_list.sort(key=len)
print(fragment_list)

