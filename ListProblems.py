l = [10,2,3,6,5]
#Sum of all element
x = 0
for n in l:
    x = x + n
print("Addition" ,x)
#Multiplication of all element
x = 1
for n in l:
    x = x * n
print("Mutilpication ",x)
#smallest no 
x = l[0]
for n in l:
    if x > n:
        x = n
print("Smallest ", x)
#Finding String
li = ['abc', 'xyz', 'aba', '1221']
for n in li:
    if n[0] == n[len(n)-1]:
        print(n)
#Increasing order with tuple
#l = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#for n in l:
#   for m in n:

#Clone or copy list
cl = list()
for n in l:
    cl.append(n)
print(cl)
