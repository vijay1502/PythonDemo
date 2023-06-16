from itertools import permutations
if __name__ == '__main__':
    stri = input()
data=stri.split()[0].upper()
n=int(stri.split()[1])
l=sorted(list(permutations(data,n)))
print(l)
for a in l:
    j=0
    value=''
    while j<n:
        value+=a[j]
        j+=1;
    print(value)
