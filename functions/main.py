def MyFunc(a):
    sum=a+1
    return sum
c=MyFunc(3)
print(c)

# no argument function 
def fun_msg():
    print(" we are calling a non returning function ")
fun_msg()

#  a function which print list item by usin for loop
# Function to print list items
def print_list_items(my_list):
    for item in my_list:
        print(item)

# Function to calculate the sum of list elements
def sum_list_elements(my_list):
    return sum(my_list)

# Function to calculate the average of list elements
def average_list_elements(my_list):
    return sum(my_list) / len(my_list)

# Function to find the maximum value in a list
def find_max(my_list):
    return max(my_list)

# Function to find the minimum value in a list
def find_min(my_list):
    return min(my_list)

# Function to count occurrences of a specific value in a list
def count_occurrences(my_list, value):
    return my_list.count(value)

# Function to filter list elements based on a condition
def filter_list(my_list, condition):
    return [item for item in my_list if condition(item)]

# Function to sort a list in ascending or descending order
def sort_list(my_list, ascending=True):
    return sorted(my_list) if ascending else sorted(my_list, reverse=True)

# Example list
my_list = [3, 5, 2, 8, 1, 5, 9, 7]

# Demonstrate the functions
print("List items:")
print_list_items(my_list)

print("\nSum of list elements:", sum_list_elements(my_list))

print("Average of list elements:", average_list_elements(my_list))

print("Maximum value in the list:", find_max(my_list))
print("Minimum value in the list:", find_min(my_list))

value_to_count = 5
print(f"Occurrences of {value_to_count} in the list:", count_occurrences(my_list, value_to_count))

condition = lambda x: x % 2 == 0  # Filter even numbers
print("Even numbers in the list:", filter_list(my_list, condition))

print("Sorted list in ascending order:", sort_list(my_list))
print("Sorted list in descending order:", sort_list(my_list, ascending=False))

