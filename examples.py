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
qoutient = x/y
debug('sum', sum)
debug('dif', dif)
debug('product', product)
# to prevent from floating type casting a floating point number decimal to int 
debug('qou',int(qoutient))

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

is_not_equal = z != 5
debug('is_not_equal', is_not_equal)


















# lets go the extra mile 
# def testFunc(num):
#     if num > 2 :
#         print('give me a number = 2 or less tahn 2')
#     else :
#         return print('this is what i want ')    
# testFunc(3)
# testFunc(1)
# testFunc(2)
# testFunc(8)

