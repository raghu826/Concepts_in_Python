from array import *

data = array("i", [])

val = int(input("length of the array:"))

for i in range(val):
    p = int(input("Enter array values:" ))
    data.append(p)


a = print("original array: ", data)

# b  = data.reverse()
# print(data)

# find out the index when enter the value in the array
# v = int(input("Enter the value in the array:"))

# k = 0
# for i in data:
#     if v == i:
#         print(k)

#     k += 1


# delete the element with index value 2

# for i in range(len(data)):
#     if i == 2:
#         d = data.pop(i)
#         print("array after deleting index value 2:", data)
#         break


# copy the array

arr = array(data.typecode, (a**3 for a in data))

print("copied array:" , arr)

