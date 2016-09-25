print (abs(100))
print (abs(-99))

print (max(1,2))

a =abs
print (a(-1))
n1 =255
n2  =1000
print(type(hex(n1)))
print((hex(n1)))
print ((hex(n2)))

def my_abs(x):
    if x >=0:
        return x
    else:
        return -x

a = my_abs(-33)
print a



def power(x, y=2):
    s = 1
    for i in range(y):
        s = s * x
    return s
print (power(5))

print(power(5,5))

def enroll(name, gender, age= 6, city='toronto'):
    print 'name :' , name
    print 'gender :' ,gender
    print 'age: ', age
    print 'city: ', city


enroll('jiang', 'girl')
enroll('man', 'boy', 7)
enroll ('john','boy',city='ottwon')

def calc(*numbers):
    sum =0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1,2,100)
nums = [1,2,3]
print calc(*nums)


def person(name,age,**kw):
    print ('name:', name,'age: ', age, 'other', kw)


person('jiang',39, city='beijing' )

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print fact(100)


