d = {'Michael': 95, 'Bob': 75, 'Tracy':85}
print d['Michael']
d['Adam']= 67
print d
d['Jack'] = 33
print d
d['Jack'] = 44
print d

print ('Michael' in d)
print(d.get('thomas', -1))

d.pop('Tracy')
print d

s = set([1,2,3])
print s

s.add(4)
print s
s.add(4)
print s
s.remove(4)
#l = ['a','b']
#s.add(l)
print s


s1 = set([1,1,2,3,4,3])
print s1

a='abc'
b = a.replace('a','A')
print b
print a

s2=set([1,2,(3,4)])
print s2
