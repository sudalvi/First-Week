a = set(["sam", "ram"])
b = set(["ram", "shyam"])
#intersection
c = a & b
print(c)
#union
c = a | b
print(c)
#differance
c = a - b
print(c)
#symetric differance
c = a ^ b
print(c) 
#remove set
a.clear()
print("Set A is " , a)