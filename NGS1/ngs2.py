#!/usr/bin/env python3

#script taken from https://github.com/CBB752Spring2016/CBB752_Final_Project_1.3/blob/master/QualityTrim.py
#modified by Nathalia

#Trims the 3' end of reads using sliding window averageQ-score threshold

import re
import numpy
import statistics

f = open('pfb.fastq', 'r')
s = open('qscores.txt', 'r')

for scores in s:
        scores = s.readlines()
        for score in scores:
                ascii_phred = score.strip().split("|")


for line in f:
	input = f.readlines()
	for line in input:
		line = line.strip()
		#
		for i in range(0,len(input),4):
			q_ascii_i = list(input[i+3])
			q_score_i = []
			window = 4
			for each in q_ascii_i:
				if each == score[0]
					active_each = each[]
					if active_each not in q_score_i:
						q_score_i[active_each] = ''
							
#q_score_i.extend(map(int,scores[numpy.where(scores==each)[0],1]))	
			for j in range(


fastq=[]
fasta=[]
