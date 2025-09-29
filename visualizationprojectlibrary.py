import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 6, 9]
y = [99, 86, 87, 88, 100, 86]

plt.scatter(x, y, color="red")
plt.title("Scatter Plot Example")
plt.show()


import matplotlib.pyplot as plt

categories = ["A", "B", "C"]
values = [10, 20, 15]

plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.show()


import matplotlib.pyplot as plt

data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram Example")
plt.show()


import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("fmri")
sns.lineplot(x="timepoint", y="signal", data=data)
plt.title("Seaborn Line Plot")
plt.show()


data = sns.load_dataset("mpg")
sns.scatterplot(x="horsepower", y="mpg", hue="origin", data=data)
plt.title("Seaborn Scatter Plot")
plt.show()


data = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=data)
plt.title("Seaborn Bar Plot")
plt.show()


data = sns.load_dataset("penguins")
sns.histplot(data["flipper_length_mm"], kde=True)
plt.title("Seaborn Histogram with KDE")
plt.show()


import numpy as np

data = sns.load_dataset("iris")
corr = data.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Seaborn Heatmap")
plt.show()


