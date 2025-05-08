# Class

# class Student: # this is class
#     name = "faiza" 

# s1 = Student()  # this is object
# print(s1.name)

#######################################################################
#Class
# class Car:
#     color = "purple"
#     brand = "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

#############################################################################

# Constructor
# class student:
#     def __init__(self, fullname):
#         self.name = fullname
#         print ("adding new student in database")

# s1 = student ("faiza")
# print(s1.name)

#####################################################################################

# class Fruits:

#  def __init__(self, name, fruits):
#     self.name = name
#     self.fruits = fruits

# fruit1 = Fruits("mango","lichi") # variables programming k andar attributes khate hai
# print(fruit1.name, fruit1.fruits)

#################################################################################

# class  Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s1 = Student("meerub", 96)
# print(s1.name, s1.marks)
     
#############################################################################################
# constructor
# class  Student: # class
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student", self.name, self.marks)

# s1 = Student("meerub", 96) # class of object
# s1.welcome()

#############################################################################################


# lets practice questions:
# Q1: Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_average(self):
#         sum = 0  # using for loop
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg score is:", sum /3 )

# s1 = Student("meerub",[77, 88, 99])
# s1.get_average()

#############################################################################################

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print("Hi", self.name, "your avg  score is:", sum/3)

# s1 = Student("meerub",[77, 83, 96])
# # s1.get_avg()

# s1.name ="zoha"
# s1.get_avg()


#############################################################################################
      
# Abstraction:
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True
#         self.clutch = True
#     print("car started...")

# car1 = Car()
# car1.start()

#############################################################################################
     

# lets practice
# Q2: Create Account class with 2 attributes- balance & account no.
# Create methods for debit, credit & printing the balance. 

# class Account:
#     def __init__(self, balance, acc):
#         self.balance = balance
#         self.account_no = acc

# # debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance = ", self.get_balance())

# # credit method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance = ", self.get_balance())

# # printing the balance
#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)


#############################################################################################


# delete method

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("faiza")
# print(s1.name) # call the name faiza

# del s1.name
# print(s1.name) # AttributeError: 'Student' object has no attribute 'name'
                 
                 
#############################################################################################

# private (like) attrubutes
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     # def reset_pass(self):
#     #     print(self.__acc_pass)

# acc1 = Account("12345", 'abcd')
# print(acc1.acc_no)
# print(acc1.__acc_pass) # agr humai kise value ko show naa karwana ho tu (undersope) ka used karte hai __

#############################################################################################


# class Person:
#     __name = "anonymous" # ya method private is lia hai kyu k humne yaha per uderscope ko used kia hai

# p1 = Person()
# print(p1.__name) # AttributeError: 'Person' object has no attribute '__name'

#############################################################################################


# class Person:
#     __name = "anonymous"

#     def __hello():
#      print("hello person!")  # message ko private banane ka tarika
      

# p1 = Person()
# print(p1.__hello()) # AttributeError: 'Person' object has no attribute '__hello'


#############################################################################################



# class Person:
#     __name = "anonymous"

#     def __hello(self):
#        print("hello person!")  # message ko private banane ka tarika

#     def welcome(self):
#         self.__hello()
        
# p1 = Person()
# print(p1.welcome()) # hello person! None


#############################################################################################

# Inheritance:
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("civic")

# print(car1.name) # fortuner
# print(car1.start()) # car started...


#############################################################################################


# multi-level inheritance class
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# Car1 = Fortuner("diesel")
# Car1.start()


##########################################################################################

# multiple inheritance
# class A :
#     VarA = "welcome to class A"

# class B :
#     VarB = "welcome to class B"

# class C (A,B):
#     varC = "welcome to class C"

# c1 = C ()
# print(c1.VarB)
# print(c1.varC)
# print(c1.VarA)

##########################################################################################

# super() method:

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(Car):
#     def __init__(self,name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)
    

##########################################################################################

# class method: ( class method mai hum self ki jaga class used karen gen.)
# class Person:
#     name = "anonymous"

#     def changeName(self,name):
#         self.name = name

# p1 = Person()
# p1.changeName("warsa")
# print(p1.name) # warsa
# print(Person.name) # anonymous


##########################################################################################


# class Person:
#     name = "anonymous"

#     def changeName(self,name):
#         Person.name = name

# p1 = Person()
# p1.changeName("warsa")
# print(p1.name) # warsa
# print(Person.name) # warsa

############################################################################################

# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls,name): # @classmethod mai self ki jaga class used hoga
#         cls.name = name
     

# p1 = Person()
# p1.changeName("warsa")
# print(p1.name) # warsa
# print(Person.name) # warsa

#####################################################################################
# property:
# class Student:
#     def __init__(self, chem, phy, math):
#         self.chem = chem
#         self.phy = phy
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"


# stu1 = Student(77, 88, 66)
# print(stu1.percentage) # 77.0%

# # reassign value
# stu1.math= 98
# print(stu1.percentage) # 87.666666667%

    
###################################################################################################

# polymorphism means ak check ko bhot ziyda tarika se used karna
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

# num1 = Complex(1, 5)
# num1.showNumber()

# num2 = Complex(2, 7)
# num2.showNumber()

###################################################################################################

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2): # num1,num2  # used for dunder function underscore __
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    

#     def __sub__(self, num2): # num1,num2  # used for dunder function underscore __
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(1, 5)
# num1.showNumber()

# num2 = Complex(2, 7)
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()


#######################################################################################

# lets practice:
# Q: Define a circle class to create with radius r using the constructor.
# Define an Area() method of the class which calculators the area of the circle.
# Define a perimeter()  method of the class which allows you to calculate the perimeter
# of the circle.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self): # area hota hai  πr²
#         return (22/7) * self.radius ** 2  # 22/7 =  3.142857
    
#     def perimeter(self): # Formula hai: 2πr
#         return 2 * (22/7) * self.radius  # 21*21 = 441 * 22/7 = 1,386

# c1 = Circle(21)
# print(c1.area()) # 1386.0
# print(c1.perimeter()) # 132.0
                 

###################################################################################################

# lets practice:

# Define a Employee class with attributes role, department & salary. This class also  a
# showDetails() method.

# create an Engineer class that in herits properties from Employee &  has additional
# attribute: name & age.

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self .salary = salary

#     def showDetail(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#             super().__init__("Engineer", "IT", "75,000")

# engg1 = Engineer("Elon Musk", 40)
# engg1.showDetail()

################################################################################################3

# lets practice:
# Q: Create a class called order which stores item & its price.
# Use Dunder function __gt__to convey that:
# order1 > order2 if price of order1 > price of order2

# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, ord2):
#         return self.price > ord2.price

# ord1 = Order("chips", 60)
# ord2 = Order("biscults", 40)

# print(ord1 > ord2) # True

#################################################################################



