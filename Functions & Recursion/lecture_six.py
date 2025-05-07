# function defination:
# def calc_sum(a,b): # parameters
#     sum = a+b
#     print(sum)
# calc_sum(5,10) # function call; arguments


# def calc_sum(a , b):
#     return a + b
# result = calc_sum(10, 15)
# print(result)

# def any_name():
#     print("faiza sheikh")

# output = any_name() # jo function return mai kuch return nhi karta aus ki value ho k ati None
# print(output) # None

# average of 3 numbers:
# def average_num(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)

# average_num(1,2,3)

# function product:
# def calc_product(a=3, b=6):
#     print (a * b)

# calc_product()
    

# lets practice:
# Q1: WAF to print of a list. (list is the parameters)

# answer:
# frds = ["meerub", "khatija","sheikh", "Ali", "osama"]
# fruits = ["orange", "lichi", "kiwi", "strawberry", "plums","mango"]
# def print_len(list):
#    print(len(list))

# print_len(frds)
# print_len(fruits)


# Q2: WAF to print the elements of a list in a single line.(list is the parameters):

# answer:
# frds = ["meerub", "khatija","sheikh", "Ali", "osama"]
# def print_frds(list):
#     print(list)

# print_frds(frds)

# answer:
# frds = ["meerub", "khatija","sheikh", "Ali", "osama"] # make list
# def print_frds(list): # make function parameter
#     for item in list: # make for loop
#         print(item, end=" ")
# print_frds(frds) # call function



# Q3: WAF to find the factorial of n. (n is the list)

# answer:

# def calc_fact(n):
#     fact =1
#     for i in range( 1, n+1):
#         fact *= i
#     print(fact)

# calc_fact(5)


# Q4: WAF to convert USD tO INR

# answer:
# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "USD =", inr_val, "INR")

# converter(1)
    
# define function even odd:
# def print_num(num):
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")

# user_input = int(input("Enter a number: "))
# print_num(user_input)

# import time
# def print_name(name):
#     for i in range(1, 10):
#         print(name, i)
#         time.sleep(2) # Delay execution for a given number of seconds. The argument may be
#  # a floating-point number for subsecond precision. 

# user_input = input("Enter a name: ")
# print_name(user_input)




# import time
# def print_name(name, count, delay):
#     for i in range(count):
#       print(name)
#       time.sleep(delay)

# user_input = (input("Enter a number: "))
# repeat_count = int(input("How many times to print the name? "))
# delay_time = float(input("Delay between prints (in seconds): "))

# print_name(user_input, repeat_count, delay_time)



#  Recursive Function:
# def show(n):
#     if(n == 0): # Base case
#         return
#     print(n)
#     show(n-1)

# show(3)



# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     else:
#         return fact(n-1) * n
    
# print(fact(2))

# lets practice:
# write a recursive function to calculate the sum of the first n natural numbers.
# answer:

# def calc_sum(n):
#     if (n == 0):
#         return 0
#     return calc_sum(n-1) + n

# result = calc_sum((5))
# print(result)

# Q:2 write a recursive function to print all elements in a list.
 # Hint: use list & index as parameters:

# answer:




