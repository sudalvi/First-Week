# Ace from pack Card 
s=0
tries=0
for prob in range(1,53):
    if prob < 17:
        s+=1
    tries+=1
print ("Ace from pack Card ",float(s)/tries)

#Second Ace after drawing a king
s = 0
tries = 0
for pb in range(2,53):
    if pb < 6:
        s += 1
    tries += 1
print("S ", s)
print("tries ", tries)
print("Ace after drawing a king ",float(s)/tries)

#Coins for HHH
s = 0
tries = 0
for pb in range(1,9):
    if pb < 2:
        s += 1
    tries += 1
print("Coins for HHH ",float(s)/tries)

#exactly one heads
s = 0
tries = 0
for pb in range(1,9):
    if pb < 4:
        s += 1
    tries += 1
print("Exactly one heads",float(s)/tries)

#least two heads
s = 0
tries = 0
for pb in range(1,8):
    if pb < 5:
        s += 1
    tries += 1
print("Least two heads",float(s)/tries)
