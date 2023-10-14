a=("this is string")
print(type(a))
My_touple=(1,2,3," hi ", 3.14, True)
print(My_touple)
print(My_touple[1]) # we can print this using index and make sure that index of a list ,array, touple star with 0
print(My_touple[5])
print(My_touple[-1])# it will start printing from reverse direction by using index
print(My_touple[-4])
print(len(a))

# now lets try some difficult task 
touple1=(1,2,3.3,"this is touple 1",88,9)
print(touple1[1:])# now it will print from index 1 to rest of the indexes 
print(touple1[:6])
print(touple1[1:6])# now it will print index 1 , and length of the element like here is 6, 
print(touple1[1::2]) # now it will print from index 1and skip one index to the rest of the indexes 

#now for nesting of the touples 

touple2=(2,3,4,5,6,7,"hi ")
touple3=(8,9,10,11,"yes")
touple4=(touple2,touple3) # here the index of touple 4 are 0,1 touple2 is at 0,and touple3 is at index 1
print(touple4)
print(touple4[1])# it will print touple four and index 1 which is touple3 

print(len(touple4[1]))

# we can add touples togather by assign them to another touple like
touple5=touple2+touple3
print(touple5 )# the result will be in one bracket it means only one touple 
