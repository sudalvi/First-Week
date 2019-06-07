#create a tuple
t = tuple()
print(t)
#tuple with differant data type
t = ("Sam", 10 , 2.5, True)
print(t)
#unpack tuple
t = (5,10,15,20,25)
a,b,c,d,e = t
print("Unpacked tuple " ,a,b,c,d,e)
#convert list to tuple
l = [1,5,9,63,2]
tup = tuple(l)
print(tup)
print(l[4])
print(l[len(tup)-5])
#revewrse of tuple
r = reversed(tup)
print(tuple(r))
