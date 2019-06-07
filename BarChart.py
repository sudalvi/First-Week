import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
pos = [ i for i , _ in enumerate(x)]
plt.bar(pos, popularity, color =(0.4, 0.6, 0.8, 1.0), edgecolor="blue")
plt.xticks(pos, x)
plt.minorticks_on()
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("Bar Chart For Programing Language Poularity")
plt.grid(which="major", linestyle='-', linewidth='0.5', color="red")
plt.grid(which="minor", linestyle=":", linewidth='0.5', color="black")
plt.show()

#Horizental Chart
y = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
pos = [ i for i , _ in enumerate(y)]
plt.barh(pos, popularity, color =['purple', 'red', 'orange', 'yellow', 'pink','cyan'], edgecolor="blue")
plt.yticks(pos, y)
plt.minorticks_on()
plt.ylabel("Language")
plt.xlabel("Popularity")
plt.title("Bar Chart For Programing Language Poularity")
plt.grid(which="major", linestyle='-', linewidth='0.5', color="red")
plt.grid(which="minor", linestyle=":", linewidth='0.5', color="black")
plt.show()

#Text Lable On Bar
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color='b')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Text Lable on Bar Chart")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which="major", linestyle="-", linewidth="0.5", color="red")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="blue")

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%f' % float(height),
        ha="center", va="bottom")
autolabel(rects1)
plt.show()

