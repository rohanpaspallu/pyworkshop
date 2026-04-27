names = ['rohan', 'sarah', 'michael', 'lisa']
# Using list comprehension to create a new list of name lengths
name_lengths = [len(name) for name in names]
print(name_lengths) 
# List of names having even number of characters
even_length_names = [name for name in names if len(name) % 2 == 0]
print(even_length_names)

upper_case_names = [name.upper() for name in names]
print(upper_case_names)

# getting range of numbers using list comprehension

print(list(range(10)))  # This will create a list of numbers from 0 to 9
print(list(range(1, 11)))  # This will create a list of numbers from 1 to 10
print(list(range(0, 20, 2)))  # This will create a list of even numbers from 0 to 18

# get squares of numbers from 0 to 9 using list comprehension
squares = [x**2 for x in range(10)]
print(squares)