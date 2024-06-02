# ******** INTRODUCTIION ******** #

# how to import and use numpy :: 
import numpy as np 
a = np.array([1,2,3])
print(a)
# print a particular index value ::
print(a[0])
# different operations perform on array ::
a1=np.array([1,2,3])
a2=np.array([1,2,3])
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)
print(a1%a2)
# different operations perform on particular index ::
print(a1[2]+a2[0]) #...etc
# two dimensional array ::
td = np.array([[1,2],[3,4],[5,6]])
print(td)

# ******** BASIC ARRAY OPERATIONS ******** #

print(td.ndim);print(a.ndim) # .ndim method is used to print dimesion of particular array :
# print item size of array ::
print(a.itemsize) # int = 4 bytes itemsize :
# print data type of array ::
print(a.dtype) # a aray has int32 data type :
# initialize same array with different data types ::
a=np.array([1,2,3], dtype=np.float64)
print(a.itemsize) # float size is 8 bytes :
# shape method give information of array dimension ::
print(a.shape);print(td.shape)
# print array with default values ::
defau_zero = np.zeros((3,4))
print(defau_zero)
defau_ones = np.ones((3,3))
print(defau_ones)
# create a list/array from some starting and finishing values ::
c_array = np.arange(1,5)
print(c_array) # don't included finishing number :
# syntax of arange : np.arange(start_index , end_index , Number_of_steps )
c_ary = np.arange(1,5,2)
print(c_ary) # work as 1,2,3,4,5 : Num_of_steps is 2 so : 1/'2'/3/'4' here 2 and 4 are not included :
# .linspace function to generate series of numbers between starting index to ending index ::
lspace = np.linspace(1,100,10) # meaning is to generate 10 numbers between 1 to 100 :
print(lspace)
# reshape function to reshape your array ::
print(td.reshape(2,3))
print(td.reshape(1,6)) #...etc
# mathm functions ::
print(a.min()) # gives minimum value :
print(a.max()) # gives maximum value :
print(a.sum()) # gives sum of all values :
# if you want to apply math func of particular row or column ::
# consider td array :
print(td)
print(td.sum(axis=0)) # give the sum of all column :
print(td.sum(axis=1)) # give the sum of all rows :
# sqrt (square root) & std (standard deviation) function ::
sqrt = np.sqrt(16); std = np.std(a)
print(sqrt); print(std)
# basic mathematical operations ::
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
print(arr1+arr2) # also do many operations :

# ******** SLICING/STACKING AND INDEXING WITH BOOLEAN ARRAYS ******** #

# slicing of one dimensional array ::
o_slc = np.array([1,2,3,4,5,6,7,8,9,10])
print(o_slc[0:6]) # print element between index 0 to 5 : 6 don't consider 
print(o_slc[-1]) # index from end starts from -1,-2.... : this will print last element :
print(o_slc[:]) # print whole array :
print(o_slc[0:]) # print 0 to end index :
print(o_slc[:10]) # print start to 9 index :
# slicing of two dimensional array ::
tslc = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(tslc)
print(tslc[1,2]) # it will print first(1) row and second(2):(0,1,2th) element :
print(tslc[0:2,2]) # it will go from firstly (0 to 1st row) and print second(2):(0,1,2th) element :
print(tslc[-1]) # print last row 
print(tslc[-1,0:2]) # print last row's 0th and 1st elements :
print(tslc[:,1:3]) # go throw all rows and prints 1st and 2nd column not print 0th column :
# print whole from for loop ::
for row in tslc:
    print(row) # it will print whole array :
# .flat fucnction : if you want to flatten a array ::
for cell in tslc.flat:
    print(cell) # flatten a array :
# verticle_stacking (.vstack) and horizontal_stacking (.hstack) function : if you want to stack/merge 2 or more arrays ::
mrg1 = np.arange(6).reshape(3,2)
mrg2 = np.arange(6,12).reshape(3,2)
merge_vertically = np.vstack((mrg1,mrg2))
merge_horizontally = np.hstack((mrg1,mrg2))
print(np.vstack(merge_vertically)) # it will merge both arrays vertically :
print(np.hstack(merge_horizontally)) # it will merge both arrays vertically :
# spliting of array : horizontal_spliting (.hsplit)and verticle_spliting (.vsplit) ::
split = np.arange(30).reshape(2,15)
print(split)
hor_split = np.hsplit(split,3) # it will split array into 3 horizontal parts :
print(hor_split)
ver_split = np.vsplit(split,2) # it will split array into 3 verticle parts :
print(ver_split)
# result is not perfect showing bcz of "array" written in result.
# so, we can print one by one split(part) of array :
print(hor_split[0])
print(hor_split[1])
print(hor_split[2])
print(ver_split[0])
print(ver_split[1])
# indexing with boolean arrays ::
ar = np.arange(12).reshape(3,4)
print(ar)
b = ar > 4 # compare all element of ar > 4 if condition is true print true else false and make a boolean array : 
print(b) # print boolean array containing true false values :
print(ar[b]) # it will print a array of true vales in b array of ar array :