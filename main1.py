
# Q1 - filter out 18+ people from dictionary 
people = [
    {"name": "Akhil", "age": 17},
    {"name": "Ravi", "age": 20},
    {"name": "Meena", "age": 22}
]   # created a dictionary

print(list(filter(lambda x: x["age"] >= 18,people))) # prints the 18+ people 


#Q2 - calculate product of the list using reduce and lambda
from functools import reduce

numbers = [1,2,3,4]

print(reduce(lambda x,y : x * y , numbers))  # calculate 2 numbers from the list every time

#Q3 - filter the even numbers and square the even nummbers

numbers = [1,2,3,4,5,6]
even  = filter(lambda x: x % 2 == 0,numbers)  # checks for the even numbers
squares = list(map(lambda y: y * y , even))  # maps the squared numbers to the list
print("the sqyare numbers of the even in list are",squares)


#Q4 - to check the string is digit 
# Lambda function
is_number = lambda x: x.isdigit()  #isdigit will check the given string

# Test cases
print(is_number("123"))  
print(is_number("abc"))   
print(is_number("12a"))  

#Q5 - to extract the date year from the data
from datetime import datetime

# Create datetime object
dt = datetime(2025, 1, 10)

# Lambda function to extract values
get_date_parts = lambda x: (x.year, x.month, x.day)

# Call function
year, month, day = get_date_parts(dt)

# Print result
print("Year:", year)
print("Month:", month)
print("Day:", day)

#Q6 - Fiboncci using lambda
# Number of terms
n = 10

# Starting values
a = 0
b = 1

# Lambda for next number
next_num = lambda x, y: x + y

print("Fibonacci series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, next_num(a, b)
