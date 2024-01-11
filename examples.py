# defining a function in python everything is based on tabs so no curly braces in this case for the function
def debug(tag, outputVal): 
    print(f'{tag} : {outputVal}')    

# variables and data types  just like js you dont really need to define the data type 
x = 5 #int 
y = 2.5 #float
debug('value of x', y)
# booleans so with bools in py you capitalize the first letter  
is_student = True
debug('is this a student', is_student)

# basic math operations 
sum = x+y
dif = x-y
product = x*y
quotient = x/y
debug('sum', sum)
debug('dif', dif)
debug('product', product)
# to prevent from floating type casting a floating point number decimal to int 
debug('qou',int(quotient))

# modulo 
remainder = 13%5
debug('remainder', remainder)

# casting boolean to string 
is_student_str = str(is_student)

debug('is_student_str', is_student_str)

# determine data types 
debug('type of x', type(x))

""" Control statement """

# if statement
age =90
if age >= 18 and age < 65 :
    print('you are an adult ')
elif age >= 65 :
    print('you are a senior citizen')       
else :print('you are a minor')    
    
#  using and/or 
is_sunny = True
is_weekend = True

if  is_sunny and is_weekend :
    print("let's go to the beach")
elif is_sunny or is_weekend :    
    print("no work to do today")
else : 
    print("let's go to work")   

# comparison operators 
a = 10 
b = 20

if a > b :
    # to pass in var you use the f string 
    print(f'{a} is greater than {b}')
      
if a < b :
    print(f'{a} is less than {b}')    

if a == b :
    print(f'{a} is equal to {b}')

z= 5 
is_greater_than_or_equal = z >= 5
debug('is_greater_than_or_equal', is_greater_than_or_equal)

# suppose to do less than butttt nope i get it 
k = 5.0 # floating point number 
is_not_equal = k != 5 # false because the computer knows its still a 5
debug('is_not_equal', is_not_equal)

# inverting booleans  will usually be used in a toggle mode 
is_teacher = True
is_teacher_not = not is_teacher

debug('is_teacher_not (inverted value)', is_teacher_not)

""" DATA STRUCTURES """
# lists (they are an ordered data structure they can contain duplicates ) their content can be modified 
my_list = ['a', 'b', 'c'] # although these are arrays we call them lists in python

# append an item to the list 
my_list.append('d')
debug('appended item in list', my_list)
debug('my_list', my_list[0])
# the last item the difference in comparison with js 
debug('my_list', my_list[-1])

# get range of items 
my_names = ['Bob', 'sam', 'charles', 'arnold']
debug('get range', my_names[1:])

# remove duplicates from list
my_list.append('a')
debug('updated list', my_list)
# set doesnt allow duplicates but we want it as a list again so we wrap the set with a list 
unique_list = list(set(my_list) )
debug('unique list',unique_list)

# tuples (they are ordered and can contain duplicates ). Their contents cannot be modified not square brackets but round brackets for tuples
my_tuple = (1,2,3,4,5)
debug('first item of tuple ', my_tuple[0])
debug('second to last item of tuple ', my_tuple[-2])


# remove dupes from tuple
my_tuple2 = (1,2,3,3,4,5)

unique_tuple = tuple(set(my_tuple2))
debug('unique tuple', unique_tuple)


# Dictionaries (they are unordered and can contain duplicates). Their contents can be modified their keys are unique and their values can be duplicated the work like objects 
my_dict = {'name': 'bob' , 'age':18}
debug('name', my_dict['name'])
debug('age', my_dict['age'])
# modifying 
my_dict['name'] = 'same '
debug('updated name', my_dict['name'])
# adding a new key value pair
my_dict['job'] = 'developer'
debug('job', my_dict['job'])

# remove key value pair 
del my_dict['job']
debug('my dict', my_dict)

""" LOOPS """
# for loops  more like for in loops 
numbers = [0,1,2,4,7,34,3543,123,657]

for number in numbers:
    debug('for loop number', number)
    if number > 30 and number <= 300:
        print('number is greater than 30 and less than or equal to  300')
    elif number > 300 :
        print('number is greater than 300')
    else:
        print('number is less than 30')      


# while loops 
count = 0
while count < 5 :
 debug('while loop count', count)
 count +=1


""" FUNCTIONS AND MODULES"""

# functions with no parameters 
def sayHello():
    print('hello')
    
    
sayHello()


# functions with parameters 
def sayHello2(name):
    print(f'hello {name.capitalize()}') # capitalizing the name 
       
sayHello2('bob')    
sayHello2('chris')    
sayHello2('richmann')    



# modules getting the math func 
import math 

debug('square root ', int(math.sqrt(25)))


""" Classes """

# create class
class Dog:
    # this here is not compulsory in py tho
    # name = ''
    # age = None  #in py we use None not null 
    
    # initializing some of the properties this object wants to use 
    # constructors this takes in params first the self meaning the scope meaning the dog class and after what ever you want to add 
     def __init__(self, name, age):
        self.name = name
        self.age = age    
    # in py you always have to pass self as the first argument even if there are no other args  so py knows it is related to this class
     def bark(self):
        print('woof') 
        
    
my_dog = Dog('bob', 5) 
debug('dog name', my_dog.name)
# calling the method 
my_dog.bark()

"""File handling"""
filename = 'example.txt'

# writing to a file 
# the open function allows you to write the file 
file = open(filename, 'w') # w means write so only write to this 
file.write('hello world this is a text file \n hjgdgshjfkdshfgvdskhvffhysvfskdj \njbdhasgdhdfgshavdgshdvgshcvghdvhvshjsdgfvjh \n djygfydskghafgagfyuyjgfihakfhfj\n ') 
file.close()


# reading entire file contents 
# with for the async sense 
with open(filename, 'r') as file:  # r for read
     content = file.read()
     debug('content', content)


# read file contents line by line 
with open(filename, 'r') as file: 
     for line in file: 
         print('single line :', line.strip())
         
#edit and append to file 
with open(filename, 'a') as file: # a as append
     file.write('\n this is a new line')

""" EXCEPTION HANDLERS """
# handle exceptions where file might not exist
try:
 with open('file_does_not_exist.txt', 'r') as file:   
     content = file.read()
     print(content)
except FileNotFoundError: #an exception that is raised when a file is not found / but you can decide not to specify and catch all
     print('file not found')  

# handle divide by 0 exceptions 



































# lets go the extra mile 
# def testFunc( num: int ):
#     if num > 2 :
#         print('give me a number = 2 or less tahn 2')
#     else :
#         return print('this is what i want ')    
# testFunc(3)
# testFunc(1)
# testFunc(2)
# testFunc('t')

