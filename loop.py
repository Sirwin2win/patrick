"""
Loop is used to iterate(count through) through a collection e.g list,tuple,set,dictionary or string. 
There are two loop types in python
1. for loop
2. while loop
"""
# a list collection
age = 20
fruits = ["Apple","Banana","Cherry","Orange"]
print(age)
print(fruits)
print(fruits[0])
# print(fruits[3])
# python for loop
for x in fruits:
    if x=='Cherry':
        print(x.upper())
    print(x)
print("******************************")
# Using the break statement (This stops the iteration when a condition is true)
for nonso in fruits:
    if nonso == "Banana":
        break
    print(nonso)
    
print("******************************")
# Using the continue statement (This skips the iteration when a condition is true)
for uche in fruits:
    if uche == "Cherry":
        continue
    print(uche)
print("******************************")
# Python while loop
names = ["Ade","Ibe","Audu","Ola"]
print(len(names))
i=0
while i < len(names):
    print(names[i])
    i += 1
print("******************************")
t = len(names)-1
while t >= 0:
    print(names[t])
    t -= 1
print("******************************")
# Looping through a string
country  = "Nigeria"
print(country[0])
print("******************************")
for x in country:
    print(x)
print("******************************")
a = 0
while a < len(country):
    
    if country[a]=="r":
        print(country[a].upper())
    print(country[a])
    a += 1
txt = "Hello World"
i = 0
while i < len(txt):
    if txt[i] == 'o':
        continue
    print(txt[i])
    i += 1