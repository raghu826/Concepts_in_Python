import numpy  as np
import time

# ar = array([1,2,3,4,4,4], int)
# print(ar)
# ar = linspace(1,100,4)  creating list using linspace
#
# print(ar)

x = range(1000000)
y = range(1000000, 2000000)



# time taken to create python list
start = time.time()
z = [(x+y) for x,y in zip(x,y)]
end = time.time()
print("time took :", (end-start)*1000 , 'z')

# a = np.array([[1, 2, 3], [4, 5, 6]]) ----- numpy array
# print(a)
#
# b= np.array([4,6,7])
# print('b:' ,b)


# time taken by numpy array
start = time.time()
c = np.arange(1000000)
end = time.time()
print("time took :", (end-start)*1000 , 'c')