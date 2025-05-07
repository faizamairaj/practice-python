# while loop
# count = 1 # Iterator
# while count <= 5:
#     print("Hello World")
#     count += 1 # iteration
# print(count)


# i = 1
# while i <= 5:
#     print(i)
#     i += 1 # output 1,2,3,4,5


# reverse while loop
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1 # output 5,4,3,2,1



# lets practice:
#Q:1 print numbers from 1 to 100.
# answer:
# i = 1
# while i <= 100:
#     print(i)
#     i += 1 

#Q:2 print numbers from 100 to 1.
# answer:
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Q:3 print the multiplication table of n.
# answer:
# i = 1
# while i <= 10:
#     print (f"5 x {i} = {5 * 1}")
#     i += 1

# num = int(input("Enter a number: "))
# answer:
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1


# Q:4 print the elements of the following list using a loop:
 # [1 ,4, 9, 16, 25, 36, 49, 64, 81, 100]

# answer:
# lst = [1 ,4, 9, 16, 25, 36,49, 64, 81, 100]
# idx = 0
# while idx < len(lst):
#     print(lst[idx])
#     idx += 1

# fruits = ["apple","mango", "banana", "grapes", "lichi"]
# index = 0
# while index < len(fruits):
#     print(fruits[index])
#     index += 1

#Q:5 search for a number x in this tuple using loop:
 # [1 ,4, 9, 16, 25, 36, 49, 64, 81, 100]

# answer:
# nums = (1 ,4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# i = 0
# while i < len(nums):
#     if (nums[i] == x):
#         print("found at index ", i)
#     else:
#         print("invalid number")
#     i += 1

# break & continue:
# i = 1
# while i <= 10:
#     print(i)
#     if(i == 5):
#         break
#     i += 1
# print("end of loop")

# i = 0
# while i <= 5:
#     if (i == 3):
#        i += 1
#        continue #skip
#     print(i)
#     i += 1


# i = 1
# while i <= 10:
#     if (i % 2 == 0):
#        i += 1
#        continue #skip
#     print(i)
#     i += 1  # even number

# i = 1
# while i <= 10:
#     if (i % 2 != 0):
#        i += 1
#        continue #skip
#     print(i)
#     i += 1 # old


# for loop:

# num = [1,2,3,4,5]
# for i in num:
#     print(i)

# name = "faiza"
# for i in name:
#  print(i)

# str = "python skills"
# for char in str:
#     if(char == 'i' ):
#      print("i found")
#      break
#     print(char)
# print("end")

   

# lets practice
# Q:1 print the elements of the following list using a loop:
 # [1 ,4, 9, 16, 25, 36, 49, 64, 81, 100]
# using for

# answer:
# list = [1 ,4, 9, 16, 25, 36, 49, 64, 81, 100]
# for i in list:
#     print(i)



#Q:2 search for a number x in this tuple using loop:
 # [1 ,4, 9, 16, 25, 36, 49, 64, 81, 100]
# using for loop

# answer:
# num = (1 ,4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# for i in range(len(num)):
#   if (num[i] == x):
#     print("found at index", i)

# range methods
# for i in range(2,100,2):
#     print(i) # even numbers
     
    
  # lets practice:
# using for & range()

#Q:1 print numbers from 1 to 100.
# answer:
# for i in range(1,101):
#     print(i)


# Q:2 print numbers from 100 to 1.
# answer:
# for i in range (100, 0, -1):
#     print(i) 


# Q:3 print the multiplication table of a number n.
# answer:
# num =int(input("Enter a number: "))
# for i in range(1 , 11):
#     print(f"{num} x {i} = {num * i }")

# for i in range(5):
#    pass
# print("some usefull work")
   


# lets practice:
# Q:1 WAP to find the sum of first natural numbers. (using while)
# answer:
# n = 5
# sum = 0
# i = 1

# while i <= n:
#    sum += i
#    i += 1
# print("total sum =", sum)



# ANSWER:
# n = 5
# sum = 0

# for i in range( 1, n+1):
#     sum += i
#     print("total sum =", sum)

# Q:2 WAP to find the factorial of first natural numbers.(using for)
# answer:

# n = 4
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i +=1
#     print("factorial =", factorial)

# answer:
# n= 5
# factorial = 1  # means multiply karna
# for i in range(1, n * 1):
#     factorial *= i
#     print("factorial =", factorial )







# for loop
# for i in range(1,6):
#   print("python developer")
# print(i) # output 5
# print(i + 1) # output 6

# nested loops:
# for i in range(5):
#     for j in range(5):
#         print(i, j)
#     print("i:", i)
#     print("j:", j)



# for i in range(1,6,2):
#     print(i) # [1,3,5]


# for i in range(5,1,-1):
#     print(i) # [5,4,3,2]
       
        
  
# for i in range(3):
#   print(i, end="") # 012
    
for i in range(1, 5, 2):
  print(i) # 1,3
    