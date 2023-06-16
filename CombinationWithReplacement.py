# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    stri = input()
data=stri.split()[0].upper()
n=int(stri.split()[1])
l=list((combinations_with_replacement(sorted(data),n)))
for a in l:
    print(''.join(a))