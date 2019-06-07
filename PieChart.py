import matplotlib.pyplot as plt
import pandas as pd
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0,0,0,0.1,0,0)
plt.pie(Popularity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart For Programing Languages", bbox={"facecolor":"0.8", "pad":5})
plt.show()

# pie chart of gold medal achievements
df = pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1,0,0,0,0)
plt.pie(medal_data, explode=explode, labels=country_data, autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()

