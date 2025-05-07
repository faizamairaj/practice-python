# marks = [66.4, 77.8, 55.9, 98.2, 75.5]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ['meerub', 23, 'karachi']
# print(student[0])
# student[0] = "faiza"
# print(student)

# list of slice
# marks = [66, 77, 88, 99, 55]
# print(marks[1:4])

# marks = [66, 77, 88, 99, 55]
# print(marks[:4])

# marks = [66, 77, 88, 99, 55]
# print(marks[1:])

# marks = [66, 77, 88, 99, 55]
# # print(marks[-4:-3])
# print(marks[-4:-1])

# list methods
# list = [1,2,3,4]
# list.append(5)
# print(list)

# list = [4,2,1,3]
# print(list.append(5))
# print (list.sort())
# print(list)

# list = [4,2,1,3]
# print(list.append(5))
# print (list.sort(reverse=True))
# print(list)

# list = ["banana", "lichi", "apple", "mango"] # decending order
# print(list.sort())
# print(list)

# list = ["banana", "lichi", "apple", "mango"] # decending order
# print(list.sort(reverse=True))
# print(list)

# list = ['a', 'd', 'e', 'f', 'c', 'b']
# list.reverse()
# print(list)

# list = [2,1,3] # index,element
# list.insert(1,5)
# print(list)

# list = [2,1,3,1]
# list.remove(1)
# print(list)

# list = [2,1,3,5]
# list.pop(2) #index remove
# print(list)

# Tuples in python
# tup =(2,1,3,4,5)
# print(tup[0])
# print(tup[1])
#tup [0] = 45 # cannot change immutable

# tup = (1.0,)
# print(tup)
# print(type(tup))

#tuple slicing
# tup = (1,2,3,4,5)
#  print(tup[1:4])

# tup = (1,2,3,4,5)
# print(tup[1:3])

#Tuple Methods
# tup = (1,2,3,4,5) # 0, 1, 2, 3, 4 
# print(tup.index(2))

# tup = (1,2,3,4,5,2,2) # 0, 1, 2, 3, 4 index value
# print (tup.count(2)) # 2 is element value

# practice questions
#Que1: WAP to ask the user to enter names of their 3 favourite movies & store them in a list
# user = (input("Enter first movie"))
# user = (input("Enter second movie"))
# user = (input("Enter third movie"))
# list = ["titanic", "english movies", "7 shades of love"]
# print(list) 

#Q:2 WAP to check if a list contains a palindrome(mean aise chezen jo samne se aur pichay se same hoti hai jaise k "ma'am"  "racecar") of elements.(Hint: usecopy() method)

# list1 = [1, 2, 1] # palindrome
# list2 = [1, 2 ,3] # non-palindrome

# list1 = [1, 2, 1]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if (copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palidrome")


# list1 = [1, 2 ,3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if (copy_list1 == list1):
#     print("palindrome")
# else:
#     print("not palidrome")


#Q:3 WAP to count the numbers of students with the "A" grade in the following tuple.
#["C" , "D", "A", "A", "B", "B", "A"]

# student_grade = ("C","D","A", "A","B","B","A")
# tup = student_grade.count("A")
# print(tup)

#Q:4 WAP store the above values in a list & sort them from "A" to "D".
# list = ["C","D","A", "A","B","B","A"] # ascending order
# (list.sort())
# print(list)










