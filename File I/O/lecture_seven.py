# file = open("demo.txt", "w")
# file.write("hello world!")
# file.close()



# file = open("demo.txt", "a")
# file.write("\nI want eat something I'm hungery! ")
# file.close()

# file = open("demo.txt", "r")
# text = file.read()
# print (text)
# file.close()



# file = open("demo.txt", "r+")
# text = file.readline()
# print (text)
# file.close()


# file = open("demo.txt", "r+")
# file.write("abc")
# print(file.read())
# file.close()



# file = open("demo.txt", "w+")
# # file.write("abc")
# print(file.read())
# file.write("meerub")
# file.close()


# file = open("demo.txt", "a+")
# print(file.read())
# file.write("meerub")
# file.close()



# with open("demo.txt", "r") as file:
#     text = file.read()
#     print(text)


# with open ("demo.txt","w") as file:
#     file.write("new data")



# import os
# os.remove("demo.txt") # file deleted



# lets practice:
# Q1: create a new file "practice.txt" using python.Add the following data in it:
# Hi everyone
# we are learning file I/O 
# using java
# I like programming in java

# answer:
# with open("practice.txt", "w") as file:
#  file.write("Hi everyone\nwe are learning file I/O\nusing java\nI like programming in java\n")
 


# Q:2 WAF that replace all occurance of "java" with "python" in above file.
# answer:

# with open("practice.txt", "r") as file:
#     text = file.read()

# new_data = text.replace("java", "Python")
# print(new_data)
 
# with open("practice.txt", "w") as file:
#     file.write(new_data)
    
  

# Q:3 search if the word "learning" exists in the file or not

# answer:
# word = "learning"
# with open ("practice.txt", "r") as file:
#     data = file.read()
#     if (word in data):
#         print('found')
#     else:
#         print("Not found")



# Q:4 WAF to find in which line of the file does the word "learning" accur first.
# print-1 if word not found.

# answer:

# def check_for_line(): 
#   word = "learning"
#   data = True
#   line_no = 1
#   with open("practice.txt","r")as file:
#     while data:
#         data = file.readline()
#         if(word in data):
#             print(line_no)
#             return
#         line_no +=1
#   return -1 

# print(check_for_line())
        



#Q:4 From a file containing numbers separated by comma, print the count of even numbers.

# amswer:
# count = 0
# with open ('practice.txt','r') as file:
#     data= file.read()

#     nums = data.split(",")
#     for val in nums:
#         if (int(val) % 2 ==0):
#             count +=1

# print(count)



