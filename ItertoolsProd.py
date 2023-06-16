from itertools import product
from itertools import permutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    A = map(int, input().split())
    B = map(int, input().split())
ls=list(A)
ls2=list(B)
for i in list(product(ls,ls2)):
    print(i,end=" ")
data=stri.split()[0].upper()
n=int(stri.split()[1])
l=sorted(list(permutations(data,n)))
print(l)
for a in l:
    print(a[0]+a[1])
