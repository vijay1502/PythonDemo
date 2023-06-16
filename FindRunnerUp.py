if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

t=tuple(arr)
print(hash(t))
s=sorted(set(arr),reverse= True)
list=arr;
