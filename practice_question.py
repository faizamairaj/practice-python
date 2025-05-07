
# n = int(input("Enter base number: "))
# power = int(input("Enter exponent: "))
# result = n ** power
# print("Result:", result)



# data = bytearray([10, 20, 30, 40])
# view = memoryview(data)

# print(view[1])     # Output: 20
# view[1] = 99
# print(data)        # Output: bytearray(b'\ncd(')






# scores = {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}

# # Using for loop to print each student's name and score
# for student, score in scores.items():
#     print(f"{student} scored {score}")

# {'Alice scored 85', 'Bob scored 90' ,'Charlie scored 78, David scored 92'}

# {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92} 
# {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}
# {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}
# {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}
# {"Alice": 85, "Bob": 90, "Charlie": 78, "David": 92}



# print(5 + 3 *2) # output 11

# print(10 % 3) # output 9


# text = "faiza learn to python"
# result = text.split()
# print(result) # ['faiza', 'learn', 'to', 'python'] (split method chezon ko torta hai)

# print(int(10.99))# 10

# print(bool(-5)) # True

# print(float(5)) # 5.0
# print (int('10')+ float('5.5')) # 15.5

# print(bool(0.0)) # False

# print(int(3.9)+ (float(2))) # 5.0

# print(bool("")) # False

# print(bool(5 == 5.0)) # True

# print(int('3.5')(int('3.5'))) # ValueError: invalid literal for int() with base 10: '3.5'

# print(2**3**2) # 512
# 2x2x2= 8
# 8x8x8 = 512

# print(-3**2) # -9

# print (int(5.8) + float(3)) # 8.0

# print (True or False) # True
# print (False or True) # True # OR har haal mai True he btata h
# print(False or False) # False
# print(True or True) # True


# print (not False or False) # True
# print (not True or True) # True
# print (not True or False) # False
# print (not False or True) # True # not kia karta hai true ho tu false kar dyte hai aur false ho tu true kar dyte hai

# print(False and True) # False
# print(True and False) # False
# print(True and True) # True
# print(False and False) # False

# data = bytearray(b'faiza')
# data1 = memoryview(data)
# data1[0] = 74

# print(data) # output bytearray(b'Jaiza')

# a = bytearray (b'meerub')
# mv = memoryview(a)
# mv[0] = ord('k')
# print(a.decode())

# def cast_str(val):
#     try:
#         return int(val)
#     except ValueError:
#         return float(val)
# print(cast_str("5.5"))



# try:
#     x = int("abc")
# except ValueError:
#     print("Conversion error")
# finally:
#     print("Completed") # Conversion error Completed

