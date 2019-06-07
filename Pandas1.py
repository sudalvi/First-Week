import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,3,2,5,3]
plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Demo Graph")
plt.show()

#Read Data From Txt File
with open("text.txt") as f:
    data = f.read()
data = data.split("\n")
x = [row.split(' ')[0] for row in data] 
y = [row.split(' ')[1] for row in data]
plt.plot(x,y)
plt.show()

#Cross Lines Legend
x = [10,20,30]
y = [20,40,10]
plt.plot(x, y, label="Line1")
x1 = [10,20,30]
y1 = [40,10,30]
plt.plot(x1, y1, label = "Line2")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Class Line Legend")
plt.legend()
plt.show()