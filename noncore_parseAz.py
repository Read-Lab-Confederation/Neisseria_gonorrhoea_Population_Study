#!/usr/bin/python

"""
Copyright (c) 2014 Matthew Ezewudo <mezewud@emory.edu>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from string import join
import numpy
from numpy import array, corrcoef, arange

#open the clusterfile and read contents
Resis = ("NG_22_","NG_23_","NG_39_","NG_18_","NG_41_","NG_46_","NG_47_","NG_48_","NG_50_","NG_51_","NG_34_","NG_35_","NG_37_","NG_32_","NG_72_","NG_33_","NG_30_","NG_31_","NG_28_","NG_52_","NG_53_","NG_54_","NG_15_","NG_17_","NG_25_","NG_26_","NG_27_","NG_55_","NG_57_","NG_61_","NG_62_","NG_64_","NG_66_","NG_68_","NG_69_","NG_70_","NG_71_","NG_73_","NG_74_","NG_75_","NG_76_")
Sensi = ("NG_58_","NG_19_","NG_67_","NG_29_","NG_40_","NG_49_","NG_36_","NG_38_","NG_43_","NG_44_","NG_24_","NG_16_","NG_20_","NG_21_","NG_59_","NG_60_","NG_63_","NG_77_")
res=0
sens=0
str2=""
fh1 = open('NG_12_19_All_Clusters.txt','r')
#place number of represented strains in each cluster in an array
print 'Non-core Clusters' + "\t" + 'Resistant & Present' + "\t" + 'Sensitive & Present' + "\t" + 'Resistant & Absent' + "\t" + 'Sensitive & Absent'
for line in fh1:
    fields = line.strip().split(",")
    cluster = fields[0].split("(")[0]
    info = fields[0].split("(")[1]
    genomes = int(info.split(":")[0])
    genes = int(info.split(":")[1])
    if genomes > 75 or genomes < 6 :
       continue
    fields1 = line.strip().split("\t")
    conts = fields1[1:]
    for y in conts:
        conts1 = y.split("(")[1][:-1]
        str2 += conts1
    for (x,p) in zip(Resis,Sensi):
        if x in str2:
           res += 1
        if p in str2 :
           sens += 1
    print cluster + "\t" + str(res) + "\t" + str(sens) + "\t" + str(len(Resis) - res) + "\t" + str(len(Sensi) - sens)
    res = 0
    sens = 0
    str2=""


