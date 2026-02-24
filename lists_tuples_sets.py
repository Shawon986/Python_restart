# Lists

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']

print(courses)
print(courses[0]) #this will print the first element of the list "courses"  

print(len(courses)) #this will print the length of the list "courses"
print(courses[-1]) #this will print the last element of the list "courses"

courses.append('Art') #this will add the string "Art" to the end of the list "courses"
print(courses)
courses.insert(0, 'Biology') #this will insert the string "Biology" at index 0 of the list "courses"
print(courses)
courses.insert(2, 'Chemistry') #this will insert the string "Chemistry" at index 2 of the list "courses"
print(courses)
courses.remove('Math') #this will remove the string "Math" from the list "courses"
print(courses)
courses.pop() #this will remove the last element of the list "courses"
print(courses)
courses.reverse() #this will reverse the order of the elements in the list "courses"
print(courses)
courses.sort() #this will sort the elements of the list "courses" in alphabetical order
print(courses)
courses.extend(courses_2) #this will add the elements of the list "courses_2" to the end of the list "courses"
print(courses)

courses.append(courses_2)
print(courses) #this will print the list "courses" with the list "courses_2" added as a single element at the end of the list "courses"
courses.extend(courses_2)
print(courses) #this will print the list "courses" with the elements of the list "courses_2" added to the end of the list "courses" as individual elements
courses.pop(7) #this will remove the element at index 7 of the list "courses"
print(courses)

number = [3,4,8,5,9,2,1,6,7]
number.sort() 
print(number)
number.sort(reverse=True)
print(number)
number.reverse()
print(number)
print(min(number)) #this will print the smallest element in the list "number"
print(max(number)) #this will print the largest element in the list "number"
print(sum(number)) #this will print the sum of all the elements in the list "number"

names = ['Shawon','Ritu','Fatema','Marium']


sorted_names = sorted(names) #this will create a new list "sorted_names" which is a sorted version of the list "names" in alphabetical order, while the original list "names" remains unchanged
print(sorted_names) #this will print the sorted list "sorted_names"

print(names) #this will print the original list "names" which is not modified by the sorted() function

animals = ['cat', 'dog', 'rabbit', 'hamster']

print(animals.index('rabbit')) #this will print the index of the first occurrence of the string "rabbit" in the list "animals"
print(animals.count('cat')) #this will print the number of times the string "cat" appears in the list "animals"

print('cat' in animals) #this will print True if the string "cat" is in the list "animals", otherwise it will print False
print('lion' in animals) #this will print True if the string "lion" is in the list "animals", otherwise it will print False


# for loop

for names in animals :
    print(names) #this will print each element of the list "animals" one by one using a for loop


# loop with index

for index, names in enumerate(animals, start=1) :    
    print(index , names, )  #this will print the index and the corresponding element of the list "animals" one by one using a for loop with the enumerate() function
 

fruits = ['apple', 'banana', 'cherry', 'date']

for index,items in enumerate(fruits ,start = 1):
    print(index, items)


num = ['1','2','3','4','5']

newNum = '-'.join(num)
print(newNum) #this will print the string "1-2-3-4-5" which is the result of joining the elements of the list "num" with a hyphen as a separator

newName2 = newNum.split('--') #this will split the string "1-2-3-4-5" into a list of strings using the hyphen as a separator and store it in a new variable "newName2"
print(newName2) #this will print the list ['1', '2', '3', '4', '5'] which is the result of splitting the string "1-2-3-4-5" into a list of strings using the hyphen as a separator


#Tuples

#tuples are similar to lists but they are immutable, which means that their elements cannot be changed after they are created. Tuples are defined using parentheses () instead of square brackets [].

items = ('phone', 'laptop', 'tablet')
print(items) #this will print the tuple "items"

items2 = items
print(items2) #this will print the tuple "items2" which is a reference to the same tuple "items"

# items[1] = 'desktop' #this will raise a TypeError because tuples are immutable and their elements cannot be changed after they are created


# Sets
#sets are unordered collections of unique elements. Sets are defined using curly braces {}.
unique_items = {'phone', 'laptop', 'tablet', 'phone'}
print(unique_items) #this will print the set "unique_items" which contains only unique elements

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Education'}   

print(cs_courses.intersection(art_courses)) #this will print the set of elements that are common to both sets "cs_courses" and "art_courses"
print(cs_courses.difference(art_courses)) #this will print the set of elements that are in the set "cs_courses" but not in the set "art_courses"
print(cs_courses.union(art_courses)) #this will print the set of all unique elements that are in either set "cs_courses" or set "art_courses" or in both sets
