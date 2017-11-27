from ex3 import fib
from sets import Set
import random
a = fib(11)
b=range(1,14)
print "%s\n%s"%(a,b)
#c= [x for x in a if x in b ]
d=list(Set(a).intersection(Set(b)))


e=random.sample(range(100),25)
f=random.sample(range (200),25)
g=list(Set(e).intersection(Set(f)))
print "%s\n%s\n%s"%(e,f,g)