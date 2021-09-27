"""
Katrīna Ogņennaja
27.09.2021.
"""
#Tuples
Dictionary = {'Durvis','Logs','Jumts'}
t=(1,'Māja',2,Dictionary)

print(t, end = "\n\n")

print(t[0])
print(t[1])
print(t[2], end = "\n\n")

print(t.index(1))
print(t.index(2), end = "\n\n")

Dictionary2={'Koks','Žogs','Puķes'}
t2=(1,'Pagalms',1,Dictionary2,1)
print(t2)
print(t2.count(1), end = "\n\n")

#Sets
s=set()
print(s)
s.add(1)
print(s, end = "\n\n")

s.add(2)
print(s)
s.add(2)
print(s, end = "\n\n")

s2=set([123,345,567,123,123])
print(s2)
s3=set(s2)
print(s3)