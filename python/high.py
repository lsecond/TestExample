L = []
n =1
while n <=99:
    L.append(n)
    n = n + 2
print L

print L[:3]
print L[-2:]

print L[:10:2]

print L[::5]


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print (key)

for key, v in d.items():
    print key ,v

for ch in 'abc':
    print (ch)

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance(123, Iterable)

print [x * x for x in range(1,11) if x % 2==0]

print [x + y for x in 'abc' for y in 'xyz']

import os
print [d for d in os.listdir('.')]

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print L2
