import numpy as np

a=np.array([[1,2,3,4,5,6,7],[4,5,6,7,8,9,10]])
b=np.array([1.1,2,3])
print(b)
print("data type of b is",b.dtype)
print("dimension of a is ",a.ndim)
print("itemsize of a is ",a.itemsize)
print("size of a is ",a.size)
print("size of b is ",b.size)
print("item size of b is ",b.itemsize)
#get a specific element
print("elemnt at row",a[1,1])

print("the row 1 of a : ",a[0,:])
print("the row 2 of a : ",a[1,:])
print("the colum 1 of a : ",a[:,0])
#[startindex:endindex:stepsize]
print("elements from 1st row from 2 to 4 with step size of 2 is",[a[0,1:6]])
#initializing different types of arrays
print(np.zeros((5,2)))
#all ones
print(np.ones((3,2),dtype='int32'))
# any other number
print(np.full((3,3),6))
print(np.full_like(b,3))
# n x m matrix with random numbers
print(np.random.rand(2,2))#gives float values between 0 to 1
#to covert the radom values into the integer or other data types
print(np.random.randint(0, 10, (2, 2)))  # random integers between 0 and 9
#identity
print(np.identity(3,'float'))
#repeat an array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,4,axis=0)
print(r1)
arr=np.ones((5,5),dtype='int32')
print(arr)
z=np.zeros((3,3))
z[1,1]=10
arr[1:4,1:4]=z
print(arr)