s={1,2,3,4,5,5}
print("set values are :",s)
print(s)
# here we can see that in sets the repeated value prints only once

#we can print the value of the sets by for loop
for value in s:
    print(value)
# for empty set 
section=set()
print(section)
print(type(section))
set1={}
print(set1)
print(type(set1))

#methods on the sets
cities1={
'islamabad',
"peshawar",
"karachi ",
"multan ",
"lahore",
"malakand",
"sialkot",
    
}
cities2={
    "faisalabad",
    "pindi",
    "swat",
    "malakand",
    "sialkot",
    "karachi ",
    "multan ",
    "lahore",
}
cities3=cities2.union(cities1)
print(cities3)
cities4=cities2.intersection(cities1)
print(cities4)
cities5=cities2.symmetric_difference(cities1)
print(cities5)
cities6=cities1.difference(cities2)
print(cities6)
