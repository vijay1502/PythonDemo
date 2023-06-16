import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
i=0
stry=''
while i<m:
    for j in matrix:
        stry+=j[i]
    i+=1

result=re.search('(\\w(.*)\\w)+',stry)
tout=''
for k in result.group(1):
    if k.isalnum():
      tout+=k
    else:
        tout+=' '
tb=re.sub('(\\w(.*)\\w)+','',stry)
result=re.sub(' +',' ',tout)
tb=re.sub(' +',' ',tb)
if tb!=None:
    print(result.strip()+tb.strip())
else:
    print(result.strip())