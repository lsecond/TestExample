def lazy_sum(*args):
    ax = 0
    for n in args:
        ax +=n
    return ax
l = lazy_sum(3,4,5)
print l


def lazy_sum(*args):
    def sum():
        ax =0
        for n in args:
            ax +=n
        return ax
    return sum

f = lazy_sum(3,4,5)
print f
print f()

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print f1()

print f2 ()

print f3()

print list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
