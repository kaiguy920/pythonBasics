# ***************************** 5. Dictionary Data Type *****************************
"""
-Dictionaries are the key and value pairs. Which are written with curly brackets. " { } "
 Ex :

 employeeData = {
  "name": "Anil",
  "number": "9876543210",
  "DOB": 1990
}

"""

# Create a Dictionary
employeeData={"name":"Anil","number":987654310,"DOB":1990}
print(employeeData)
print(type(employeeData))

# Access the value from dictionary
a=employeeData["number"]
print("employeeData['number'] ==> ", a)

# Update or change the value
employeeData["name"] ="Kumar"
print("changing name to Kumar", employeeData)

# Add key and value for existing dictionary
employeeData["address"]="India"
print("add key & value of address", employeeData)

# length of a dictionary
print("length = ", len(employeeData))

# Copy the dictionary to other variable
emp = employeeData.copy()
print(".copy() ==> ", emp)

# Iterate the values in dictionary
for a in employeeData.keys():
    print("for a in employeeData.keys()", employeeData[a])

# Iterate both keys and values
for a,b in employeeData.items():
    print("for a,b in employeeData.items()", a,b)

# Remove the value
employeeData.pop("address")
print("employeeData.pop('address') ==> ", employeeData)

# Clear the dictionary
employeeData.clear()
print(".clear() ==>", employeeData)

# delete the dictionary
del employeeData
#print(employeeData)
