# string 
name1 = "Ashutosh"
name = str("Ashutosh")
print(name is name1)
print(isinstance(name,str))

string ="     "
print(bool(string))
print(string.isspace())
# !is space is include this as white space ‘ ‘ – Space
# !‘\t’ – Horizontal tab
# !‘\n’ – Newline
# !‘\v’ – Vertical tab
# !‘\f’ – Feed
# !‘\r’ – Carriage return

print("---------------------------------")

# String manipulation ,however there is not possible to manipulate the string because it is imutable , so we can conver it into list and then can easily do it
string = "Hello World"
string = list(string)
print(type(string))
string[0] = "-"
print(string)
string = "".join(string)
print(string)
print("-------------------------------------------------------------")
sample = "Hello, World!"

# Find a substring
position = sample.find('World')
print(position)  # Output: 7

# Replace a substring
replaced = sample.replace('World', 'Python')
print(replaced)  # Output: Hello, Python!

# Split a string into a list
split_list = sample.split(', ') # that word is not include while split 
print(split_list)  # Output: ['Hello', 'World!']

# Join a list into a string
joined_str = ' - '.join(split_list)
print(joined_str)  # Output: Hello - World!

# Check if the string starts or ends with a substring
print(sample.startswith('Hello'))  # Output: True
print(sample.endswith('!'))        # Output: True


