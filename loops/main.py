for i in range(1, 6):  # This will iterate from 1 to 5 (6 is not included).
    print(i)
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key in person:
 print(key)
 text = "Hello"
for char in text:
    print(char)

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)


my_touple = (22,33,44,55,66)

for item in my_touple:
    print(item)

my_list = [1, 2, 3, 4, 5]

# now we are going towards while loop

# Initialize a variable to start counting
count = 1

# Set the condition for the while loop
while count <= 5:
    print(count)
    count += 1  # Increment the count by 1 in each iteration

print("Loop finished!")


# Initialize an index variable
index = 0

# Use a while loop to iterate through the list
while index < len(my_list):
    print(my_list[index])
    index += 1
