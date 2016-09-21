L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g
for n in g:
    print n

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


f = fib(100)
print f
for n in f:
    print n

def odd():
    print ('setp 1')
    yield 1
    print ('setp 2')
    yield 3
    print ('step 3')
    yield 5


o = odd()
print next(o)
print next(o)
