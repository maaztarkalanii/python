dic1={
    'name': "Maaz Ali",
   'semester': "5",
   'ID': "21pwcse2038",
   'university': 'university of engineering and technology peshawar'
   
}
print(dic1['name'])
print(dic1['semester'])
print(dic1['ID'])
print(dic1['university'])

# modifying the value of the dictionary

dic1['name']=input( "please enter your name ")
dic1['semester']=input( "please enter your current semester")
dic1['ID']=input( "please enter your ID ")
dic1['university']=input( "please enter the name of your university ")
print("your name is ",dic1['name'])
print("your current semester  is ",dic1['semester'])
print("your ID is ",dic1['ID'])
print("your university is ",dic1['university'])

# adding some new key_value pair
dic1['dob']=input("please enter your date of bith")
print("your date of birth is :", dic1['dob'] )

# getting a list of keys or values
print(list(dic1.keys()))
print(list(dic1.values()))

# for clearing the dictionary we can use dic1.clear()
# for deletion of the dictionary we can use del dic1 
