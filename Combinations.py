# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    stri = input()
data=stri.split()[0].upper()
n=int(stri.split()[1])
i=1
while i<=n:
    a=sorted(list(combinations(sorted(data),i)))
    for j in a:
        print(''.join(j))
    i += 1