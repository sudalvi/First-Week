from array import *
array_num = array("i",[4,1,7,3,4,1,5,5,2])
for i in array_num:
    if array_num.count(i) > 1:
        array_num.remove(i)
print("Values "+str(array_num)) 