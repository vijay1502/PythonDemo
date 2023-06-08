# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from numpy import *
from _functools import reduce
import CALCULATOR as c


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi('Vijay')

# print("Hello World")
# a=6
# b=5
# a,b=b,a
# print(a,b)
#
# nums=[1,2.5,"abc",'avs']
# print(nums)
#
# print(nums[10:4])
# s={1,22,3,44,556,74}
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# s={1:'Vijay',2:'Sujeet'}
# for i in s.values():
#     for j in s.keys():
#         if(s.get(j)==i):
#             print("Printed:"+i)
#
# keys=['EmpId','EmpName']
# values=[1233,'Vijay']
# data=dict(zip(keys,values))
# print(data)
# print(data['EmpId'])
# data['Location']='Bangalore'
# print(data)

nums=[12,33,22,4,60]
for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print("no number")

val=linspace(1,22,50)
print(val)
val=arange(1,12,2)
# newArr=array(val.typecode,(a*a for a in val))
# newArr.pop()
# print(newArr)
print(val)
val=logspace(2,34,6)
print(val)
newArr=val
print(newArr.dtype)

def str_int(a,b):
    d=a/2;
    c=str(b).split("i");
    return d,c

print(str_int(2,"V ,i, J A Y"))
f=lambda a,b:str(b)+a
print(f("V",2))

def is_even(n):
    return n%2==0

nums=[23,112,423,56,12]
evenNum=list(filter(lambda n:n%3==0,nums))
print(evenNum)
doubles=list(map(lambda n:n+2,nums))
print(doubles)
redder=reduce(lambda a,b:a-b,doubles)
print(redder)


def smarter(a,b):
    return a+b;
def dec_smart(func):
    def inner(a,b):
        if type(a)!=type(b):
            a=(type(b))(a)
            return "type difference not allowed",a+b
        else:
            return func(a,b)
    return inner

div1=dec_smart(smarter)
print(div1(2,"Vijay"))
print("Multiply ",c.modulo(2,4.2))

print(__name__)