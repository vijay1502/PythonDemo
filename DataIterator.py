nums=[1,4,2,33,5];
it=iter(nums)
# print(it.__next__())
# print(it.__next__())

# for i in nums:
#     print(i)

class TopTen:
    def __init__(self):
        self.digit=1;

    def __iter__(self):
        return self
    def __next__(self):
        if self.digit<=10:
            val=self.digit
            self.digit+=1
            return val
        else:
            raise StopIteration

values=TopTen()
print(next(values))
for i in values:
    print(i)