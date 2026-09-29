#functions in python
#functions are used for reusability

#function definition
def welcome_message():
    print("Welcome To Python Sessions by Bitcode Tech")   #function body

welcome_message()           #function call

#passing arguments and returning from the function
def addition(num1 : int,num2 : int) -> int:
    return num1 + num2

res_add = addition(12,14)
print("function addition result is  : ",res_add)

print("multiplication table of 12 using function")
#function definition
def multiplication_table(num : int):
    for i in range(1, 11):
        print(num * i)

multiplication_table(12)                    #function call
multiplication_table(14)                    #function call

#factorial calculation  -- recursion
def factorial(num : int):
    if num == 0 or num == 1:
        return 1
    else :
        return num * factorial(num-1)

res_fact = factorial(5)
print("function factorial result is  : ",res_fact)

#without recursion
def fact_calculator(num : int):
   fact = 1
   for i in range(2, num+1):
       fact *= i
   return fact

res_fact_1 = fact_calculator(5)
print("function factorial without recursion , result is  : ",res_fact_1)

numbers = [12,3,1,4,2, 52, 66, 87]

#sequence as an argument to a function
def sum_of_all(n : list):
    sum1 = 0
    for i in n:
        sum1 += i
    return sum1

sum_res = sum(numbers)
print("sum of all numbers in list ",sum_res)

print("----------------------")
def check_even_odd(n : list):
    for i in n:
        if i % 2 == 0:
            print(f"{i} is an even number")
        else:
            print(f"{i} is an odd number")

check_even_odd(numbers)

print("-----------------------------")
#return multiple values from a function
def maths_operations(num1 : int, num2 : int):
    sum1 = num1 + num2
    diff1 = num1 - num2
    return sum1, diff1

number1 = 100
number2 = 56
sum_result, diff_result = maths_operations(number1, number2)
print("Sum and difference of two numbers is : ",sum_result," ",diff_result)

#return control to the function and not the value
def check_even(n : int):
    if n % 2 == 0:
        return                      #returning control back to the function
    else:
        print("n is odd")

#functions as first class objects
#1. assigning function to a variable

def print_welcome_message():
    print("welcome to python session")

#print_message is a variable, we are assigning print_welcome_message function to a variable
print_message = print_welcome_message

print_message()             #calling function from function related variable

#2. writing function inside another function
def print_college_details():
    print("college details --outer function is called")
    def print_branch_details(branch):
        print("inside function branch details which is nested in college details ",branch)

    print_branch_details("AI & DS")     #function call given inside another function
    print_branch_details("AI & ML")     #function call given inside another function


print_college_details()                 #outer function call

#important
#3. higher order functions in python
numbers1 = [23,98,12,78,45,33]
#lambda
even_numbers = filter(lambda x : x % 2 == 0,numbers1)
print("---------------")
#iterate over even numbers list returned from filter function
for i in even_numbers:
    print(i)


#lambda with map function
list_1 = [10,11,12,13,14]
list_of_squares = map(lambda i : i ** 2,list_1)
list_of_cubes = map(lambda i : i ** 3,list_1)
print("-------squares of numbers from list--------")
for i in list_of_squares:
    print(i)

print("-------cubes of numbers from list--------")
for i in list_of_cubes:
    print(i)