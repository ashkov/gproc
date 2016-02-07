#!/usr/bin/python
# vim: set fileencoding=utf-8:
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("file", help="File to parse")
args = parser.parse_args()
f = open(args.file)
dic = {'G': [0,1,2,3,4,10,17,18,19,20,21,28,28.1, 30, 30.1, 38.2, 38.3, 38.4, 38.5, 40, 43.1, 49, 53,54,55,56,57,58,59, 61, 80,90,91,91.1,92,92.1, 93,94],
        'M': [0,2,3,4,5,8,9,30]
        }
def testarray(x):
    for xx in x:
        if not testcode(xx):
            print "Line: "+str(i)+", Wrong gcode:"+xx

def testcode(xx):
    if xx[0] in dic:
        if float(xx[1:]) in dic[xx[0]]:
            return True
        else:
            return False
i = 0
for line in f:
    m=re.findall('([GM]\d+(?:\.\d+)?)', line)
    testarray(m)
    i=i+1
print "Total lines: "+str(i)

