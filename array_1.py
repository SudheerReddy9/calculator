from array import *
# # creating a array
# val = array('i',[5,6,9,8,3,1])

# # creating a new array from old array
# newArrr = array(val.typecode, (a*a for a in val))
# for e in newArrr:
#     print(e)

arr = array('i',[])
n = int(input("Enter the length of array"))

for i in range(n):
    x = int(input('ENter the next value'))
    arr.append(x)
    #print(arr)
print(arr)