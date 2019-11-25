#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['t', 'F', 'T', 'f']

print (list(Unique(data1)))
print (list(Unique(data2)))

print (list(Unique (data3, ignore_case = False)))
print (list(Unique (data3, ignore_case = True)))
