
"""
The Xrange iterator class constructor takes three arguments in the following order:

start — integer or real number
end — integer or real number
step — integer or real number, default value
The Xrange iterator generates the arithmetic progression
from start to end, including start and not including end.
"""



class Xrange:
    def __init__(self,start,end,step=1):
        self.start=start-step
        self.end=end
        self.step=step
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.end-self.start)<=abs(self.step):
            raise StopIteration
        else:
            self.start=self.start+self.step
            return self.start
        
            
        
         
"""
Test examples
"""


xrange = Xrange(100.1, 13.7, -3.8)

print(*xrange)

xrange = Xrange(5.0, 56, 2.0)

print(tuple(xrange))

xrange = Xrange(24, 89, 13)

print(list(xrange))

xrange = Xrange(100, 101)

print(*xrange)

