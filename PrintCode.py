if __name__=="__main__":
    a=int(input())
    b=int(input())
print(a+b)
print(a-b)
print(a*b)

fruits=["apple","banana","grapes"]
x,y,z=fruits
print("x:",x,"y:",y,"z:",z)
tup=('2','44','543')
v=frozenset(tup)
b="Hey Vijaya"
print(b[-6:-2])

age=33
name='Vijay'
height='170cm'
ageText="My age is {} and my name is {} and my height is {}"
print(ageText.format(age,name,height))
name="vijay goood"
print(name.index('o'))


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
# 50,0,15,32,27
# 0,15,27,32,50
# 50,65,23,82,100
thislist.sort(key = myfunc)
print(thislist)

