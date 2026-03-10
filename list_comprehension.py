names = ['rohan', 'sarah', 'michael', 'lisa']
# Using list comprehension to create a new list of name lengths
name_lengths = [len(name) for name in names]
print(name_lengths) 
# List of names having even number of characters
even_length_names = [name for name in names if len(name) % 2 == 0]
print(even_length_names)