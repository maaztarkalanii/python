a=[1,2,3,4,5,6]
print(a)
b=a
print(b)
# we have a feature of assigning of the whole value of list to another list this is't availabe in touple 
c=[10]
print(a[3])
print(a[5])
print(a[-1])
print(a[-3])
print(min(a))

# we can change the index value of the list like 
a[-3]=23
print(a)# it will print 23 instead of 4 
 
# nesting of the lists
d=[a,b]
print(d)
d=[[a],[b]]
print(d)

e=[a+b]
print(e)
e=a+b
d=[a,b]
print(e)
print(len(e))

# some other operations 
print(e[1:])
print(e[:6])
print(e[1:6])
print(e[1::2]) 

 