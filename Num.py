import numpy as np
#Example Arrays a and b
a=np.array([[1,2,3,4,5,6,7],[4,5,6,7,8,9,10]])
b=np.array([1.1,2,3])
print(b)
print("data type of b is",b.dtype)#prints Datatype
print("dimension of a is ",a.ndim)#Prints Dimensions of selected array
print("itemsize of a is ",a.itemsize) #prints item size of the selected array
print("size of a is ",a.size) #prints size of array a(Number of elements)
print("size of b is ",b.size) #prints size of array b
print("item size of b is ",b.itemsize)#prints item size of the selected array
# to get a specific element
print("elemnt at row",a[1,1])
#prints the selected entire row a[row_number,:]
print("the row 1 of a : ",a[0,:])
print("the row 2 of a : ",a[1,:])
#prints the selected entire column a[:,column_number]
print("the colum 1 of a : ",a[:,0])
#prints the elemnts which are present in between other two elements [startindex:endindex:stepsize]
print("elements from 1st row from 2 to 4 with step size of 2 is",[a[0,1:6]])
#initializing different types of arrays
print(np.zeros((5,2))) #prints array containing all zeros
#prints array containing all ones
print(np.ones((3,2),dtype='int32'))
#inintialixing array of dimensions(n,m) with specific number
print(np.full((3,3),6))
#returns the array of same dimensions and size like b fills with specific number x
print(np.full_like(b,3))
# n x m matrix with random numbers
print(np.random.rand(2,2))#always gives float values between 0 to 1
#to covert the radom values into the integer or other data types
print(np.random.randint(0, 10, (2, 2)))  # random integers between 0 and 9
#returns identity matrix
print(np.identity(3,'float'))
#used to repeat an array
arr=np.array([[1,2,3]])
r1=np.repeat(arr,4,axis=0)#if the value of axis is 0 then it is column wise operations if it is 1 then it is row wise operation
print(r1)
arr=np.ones((5,5),dtype='int32')
print(arr)
z=np.zeros((3,3))
z[1,1]=10
arr[1:4,1:4]=z
print(arr)
#to print an datatype of an array
print(a.dtype)

#more operations in next file named Numpy_Operations_2
