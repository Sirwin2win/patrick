#Strings are either surrounded by a single quote or a double quote
name = 'John Doe'
text = "Today is Patrick's python class"
print(name)
print(text)
# Declaring a multiple line string
txt = '''Ways of choosing a good variable name
1. Camel Case e.g firstName="Jonh" ;lastName = "Doe"
2. Pascal Case e.g FirstName="John"; LastName="Doe"
3. Snake Case e.g first_name="John"; last_name="Doe"
Note: Variable names are case sensitive e.g name="John Doe" is not the same as Name="John Doe"
'''
txt2 = """
 Variable Scopes
 1. local scope : This a variable that exists within a block of code
 2. global scope: This is a variable that exists all over the file
"""
print(txt)
print(txt2)
students = ["Uche","Ade","Ola","Audu"]
print(students[3])
print(text[6])
for x in students:
    print(x)
# Looping through a string
for demo in text:
    pass
    # print(demo)
# Length of a string using len()
# print(len(text))
# print(len(txt))
# print(students[3])