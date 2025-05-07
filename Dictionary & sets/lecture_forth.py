# info = {
#     "name": "faiza",
#     "age": 26,
#     "subjects": ["English", "Maths", "Science"],
#     "marks": 96.5,
#     "is_adult": True,
#     "practice":"coding"
# }
# print(info)
# print(type(info))
# print(info["is_adult"])

# info["name"] = "meerub"
# print(info)

# nested dictionary
# student = {
#     "name" : "jannat",
#      "subjects":{
#          "html":97,
#          "css": 99,
#          "javascript": 77
#      }
# }
# print(student)
# print(student["subjects"]["css"])
# print(student.keys())
# print(list(student.keys())) # type casting is string, list, tuple ya float
# print(student.values())
# print(student.items())
# print(student["name1"]) # error
# print(student.get("name1")) # none
# student.update({"city": "karachi"})
# print(student)

#set in python
# collection = {1,2,3,4,5, "hello","world"}
# print(collection)
# print(type(collection)) 

# collection = {1,2,2,2,3,3, "hello","world","hello"}
# print(collection)
# print(type(collection)) # dublicate values ko ignore karna

# collection = set()
# print(type(collection)) # empty set syntax

# collection = {}
# print(type(collection)) #empty dict syntax

# set methods:
# collection = set()
# collection.add(1)
# collection.add(2)
# print(collection)

# collection = {"zoha","noor", "meerub","ramla"}
# print(collection.pop())
# print(collection.pop()) # ramdom values generate karta hai


# set methods (union, intersection, difference)
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}

# print(set1) # ya apni purani values he return karta hai
# print(set2) # ya apni purani values he return karta hai


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.intersection(set2)) # {4, 5} jo same value ho wo he ati hai

# print(set1) # ya apni purani values he return karta hai
# print(set2) # ya apni purani values he return karta hai

# let's practice question:

#  Q1: store following word meanings in  python dictionary:

# table: "a piece of furniture", "list of facts & figures"
# cat: "a small animal"

#answer:
# dict = {
# "table": ["a piece of furniture", "list of facts & figures"],
# "cat": {"a small animal"}
# }
# print(dict)

# Q:2 you are given a list of subjects for students. Assume one classsroom is required for 1 subject.
# How many classrooms are needed by all students.

# "python", "java","C++", "python", "javascript",
# "java", "python", "C++", "C", "java"

# answer:
# subjects = {
#     "python", "java","C++", "python", "javascript",
#     "java", "python", "C++", "C", "java"
# }
# print(len(subjects)) # 5 classrooms are needed

# Q:3 WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one subjects name as key & marks as value.

# answer:
# marks = {}

# sub = int(input("Enter math: "))
# marks.update({"math": sub})

# sub = int(input("Enter english: ")) 
# marks.update({"english": sub}) 

# sub = int(input("Enter urdu: "))
# marks.update({"urdu": sub})
# print(marks)

# Q:3 Figure out a way of 9 & 9.0 as separate values in a set.
# (you can take help of built-in data types)

# answer:
# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values) # {9, 9.0} # 9.0 is float and 9 is int
# print(type(values)) # set