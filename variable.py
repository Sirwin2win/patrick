'''  Ways of choosing a good variable name
1. Camel Case e.g firstName="Jonh" ;lastName = "Doe"
2. Pascal Case e.g FirstName="John"; LastName="Doe"
3. Snake Case e.g first_name="John"; last_name="Doe"
Note: Variable names are case sensitive e.g name="John Doe" is not the same as Name="John Doe"
'''
name = "John Doe"
name = "Jude Doe"
print(name,name)
"""
 Variable Scopes
 1. local scope : This a variable that exists within a block of code
 2. global scope: This is a variable that exists all over the file
"""
def greet():
    afa = "Patrick Doe" #local variable
    print("Hola, "+afa)
greet()
print(name)
