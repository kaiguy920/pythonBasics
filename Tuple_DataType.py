# ***************************** Tuple Data Type *****************************
"""
-Storing the different data type values in order and tuple is unchangeable in run time. It allows duplicate values
-values should assign to a variable in  "()"
 Ex : name_tuple = (1, "python", 2.3, 1)
"""
name_tuple = (1, 2, 3, 4, 5, "Python", 1, 2, 3, 4, 5)
print("ORIGINAL TUPLE", name_tuple)
# Access the values in a tuple tupleName[indexValue]
a =name_tuple[5]
print("name_tuple[5]==> ", a)

# Slicing - Getting the required portion of the values in the tuple  [1:n-1].
b = name_tuple[4:7]
print("slice [4:7] ==>", b)

# you can't update the value in tuple


# Length of a tuple - len()
print("length = ", len(name_tuple))

print(".count(1), occurance of 1 ==> ", name_tuple.count(1))
# You can't add a value in the tuple

# You Can't inserting a value in tuple


# You can't Remove the value from tuple


# How to find the value in the tuple
a = "Python" in name_tuple
print("python in name_tuple =  ", a)

# Iterate the tuple value
for a in name_tuple:
    print(a)

# Add two tuple items "+"
a = (1,2,3)
b=(4,5,6)
c =a+b
print("value of a + b = ", c)

# Delete the tuple
del name_tuple
# print(name_tuple)
