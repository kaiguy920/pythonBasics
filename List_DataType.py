# ***************************** 3. List Data Type *****************************
"""
-Storing the different data type values in order and list is changeable in run time. It allows duplicate values
-values should assign to a variable in square brackets "[] "
 Ex : name_list = [1, "python", 2.3, 4]

"""

name_list = [1, "python", 2.3, 4, 5, 6, 7, 8, 9]
print(type(name_list))
print(name_list)

# Access the values in a list listName[indexValue]
a = name_list[1]
print("getting index value 1 = ",a)

a = name_list[-1] #last index
print("name_list[-1] ==>", a)

# Slicing - Getting the required portion of the values in the list  [1:n-1].
b=name_list[1:5]
print("name slice [1:5] ==> ", b)

b=name_list[1:]
print("name_list slice[1:] ==> ",b)

# Update the value in list
name_list[1] ="Hello"
print(name_list)

# Length of a list - len()
print("listlength", len(name_list))

# Adding the value in the list append()

name_list.append("Python")
print("list .append() ", name_list)

# Inserting a value insert(index , "value")
name_list.insert(1,"World")
print("list .insert(1, __) ", name_list)

# Remove the value from list
name_list.remove("Hello")
print("list.remove()", name_list)

# How to find the value in the list
a = "Python" in name_list
print("'Python' in name_list ==>", a)

# Iterate the list value
for a in name_list:
    print("for a in name list", a)

# Add two list items "+"
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
print("int", int(a[1])+int(b[0]))

# Delete the list
#del name_list
print(name_list)