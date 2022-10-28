# 5 types of data
# 1. Numbers
# 2. Strings
# 3. List
# 4. Tuple
# 5. Dictionary

# *********************** 1. Numbers ***********************

a=5
b=5.2
c=5j

print(type(a)) #<class 'int'>
print(type(b)) #<class 'float'>
print(type(c)) #<class 'complex'>

# ***********************  2. Strings ***********************

name = "Python"
print(type(name)) #<class 'str'>

# *********************** 3. List ***********************

name_list = [1, "python", 2.2, 1]
print(name_list)
print(type(name_list)) #<class 'list'>

name_list[1] = "Hello"
print(name_list)

# *********************** 4. Tuple ***********************

# list of variables stored in (); cannot change in run time


tuple_list = (1, "python", 2.2, 1)
print(tuple_list)
print(type(tuple_list)) #<class 'list'>

# tuple_list[1] = "Hello" # ==> causes error
# print(tuple_list)

# *********************** 5. Dictionary ***********************
# key, value pairs

employeeData = {
    "name": "Anil",
    "number": "9876543210",
    "DOB": 1990
}

print(employeeData)
print(type(employeeData))
print(employeeData["name"])