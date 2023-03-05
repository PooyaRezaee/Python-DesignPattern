"""
    Itrator
"""

class Itration:
    def __init__(self,_min,_max):
        self.min = _min
        self.max = _max

    def __next__(self):
        if self.max == self.min:
            raise StopIteration()
        self.max -= 1
        return self.max

class Range:
    def __init__(self,_min,_max):
        self.min = _min
        self.max = _max

    def __iter__(self):
        return Itration(self.min,self.max)


r = Range(58,60)

# WAY 1
iter_r = iter(r)
print(next(iter_r))
print(next(iter_r))
print(next(iter_r))

# WAY 2
for i in r:
    print(i)
