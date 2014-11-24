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

def readProt(protfile,blastfile):
    bactnames=[]
    protarray=[]
    fh1=open(protfile)
    fh2=open(blastfile)
    for line in fh1:
        lined=line.strip()
        protarray.append(lined)
    for out in fh2:
        outed=out.strip()
        outarray=outed.split("\t")
        for access in protarray:
            if access.find(outarray[0]) != -1:
               bact=access.split("[")
               bactnames.append(bact[1][:-1])
    return(bactnames)

def readOntol(ontolfile):
    (array1,ontol) = ([],[])
    fh3 = open(ontolfile)
    for fields in fh3:
        array1.append(fields.strip())
        seqArray1 = join(array1, "")
        array2 = seqArray1.split('[Term]')
    for str in array2:
        if str.find("confers") != -1 or str.find("conferring") != -1:
           ontol.append(str)
    return(ontol)

def readDb(dbfile,blastfile):
    filehand1 = open(dbfile)
    filehand2 = open(blastfile)
    dbheaders=[]
    subject=[]
    for line in filehand1:
        line1 = line.strip()
        arrayed1=line1.split()
        arrayed2=line1.split("[")
        for str in arrayed1:
            if str.find("ARO:") != -1 and str[4] == '3': 
               v=join(arrayed1[1:4], "")
               k=join(arrayed2[1][:-1],"")
               d = arrayed1[0][1:] + ' ' + v + ' ' + k + ' ' + str
               dbheaders.append(d)
    for lined in filehand2:
        lines = lined.strip()
        fields=lines.split("\t")
        for str1 in dbheaders:
            if str1.find(fields[1]) != -1:
               subject.append(str1)
               break
    return(subject)

def main(infile1,infile2,infile3,infile4):
    parseOutput(readProt(infile1,infile3),readDb(infile2,infile3),readOntol(infile4))

def parseOutput(bactnames,subject,ontol):
    for query in range(0, len(bactnames)):
        queryed = subject[query].split()
        for keyed in ontol:
            if keyed.find(queryed[len(queryed)-1]) != -1:
               term = keyed.split('"')
               termed = term[1]
               #termed = term[5][:len(term)-1]
               print bactnames[query] + "\t" + subject[query] + "\t" + termed
               
import sys
from string import join

if __name__ == "__main__":
   main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
        