num1 = 42 ## varaible declaration , integer, float in javascript, initialize
num2 = 2.3 ## varaible declaration , float , initialize
boolean = True  ## variable declaration , boolean , value of True with capital T, initialize
string = 'Hello World' ## variable declaration , string data , initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] ## array/list declaration , initialize 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} ##  dict declaration , initialize
fruit = ('blueberry', 'strawberry', 'banana') ## tuple declation , initialize
print(type(fruit)) ## type check , print 
print(pizza_toppings[1]) ## list, access value 1, 
pizza_toppings.append('Mushrooms')##lists, add value
print(person['name']) ## dict, access value
person['name'] = 'George' ## dict , change value
person['eye_color'] = 'blue' ## dict , add value
print(fruit[2])## access value ,tuple

if num1 > 45: ## if  
    print("It's greater")## print string
else:## else
    print("It's lower") ## print string, 23<45 will print this 

if len(string) < 5:
    print("It's a short word!") 
elif len(string) > 15: ## else if
    print("It's a long word!")
else:
    print("Just right!") ## output

for x in range(5):## start 1 end 4 
    print(x)
for x in range(2,5):## start 3 end 4
    print(x)
for x in range(2,10,3): ## start 3 end 9 , increment 3
    print(x)
x = 0 ## variable declaration 
while(x < 5): ## start x = 0 end x = 4
    print(x)
    x += 1 ## increment x by one 

pizza_toppings.pop() ## delete last value 'olives'
pizza_toppings.pop(1) ## delete second value 'sausages'

print(person) ## print dictionary
person.pop('eye_color') ## remove value of 'eye_color'
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':## conditionals
        continue  ## continue
    print('After 1st if statement')
    if topping == 'Olives':
        break ## break

def print_hello_ten_times():
    for num in range(10): ## for loop start =0 end 0
        print('Hello')

print_hello_ten_times() ## print hello ten times

def print_hello_x_times(x):
    for num in range(x): ## x is the sequence
        print('Hello')

print_hello_x_times(4) ## print hello 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() ## print hello 10 times
print_hello_x_or_ten_times(4) ## print hello 4 times


"""
Bonus section
"""

# print(num3)  name <num3> is not defined
# num3 = 72 variable declaration
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])  KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean)  - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'