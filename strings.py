print("Hello world")

name = "Shawon" #this is a string variable

print(name)

print(len(name)) #this will print the length of the string variable "name"

print(name[0]) #this will print the first character of the string variable "name"

# total index = length of the string - 1

print(name[-1]) #this will print the last character of the string variable "name"

print(name[0:3]) #this will print the first three characters of the string variable "name"
print(name[0:]) #this will print all characters of the string variable "name" 
print(name[:3]) #this will print the first three characters of the string variable "name"   

print(name.upper()) #this will print the string variable "name" in uppercase letters
print(name.lower()) #this will print the string variable "name" in lowercase letters

print(name.count("o")) #this will count the number of times the character "o" appears in the string variable "name"
print(name.find("o")) #this will find the index of the first occurrence of the character "o" in the string variable "name"

newName = name.replace("Shawon", "Shawon Islam") #this will replace the string "Shawon" with "Shawon Islam" in the string variable "name" and store it in a new variable "newName"
print(newName)

greeting = "Hello, " + name + "!" #this will concatenate the string "Hello, ", the string variable "name", and the string "!" and store it in a new variable "greeting"
print(greeting)


greetings = "Hello"
names = "Shawon"

messages = '{}, {}!'.format(greetings, names) #this will format the string by replacing the placeholders {} with the values of the variables "greetings" and "names" and store it in a new variable "messages"
print(messages)


