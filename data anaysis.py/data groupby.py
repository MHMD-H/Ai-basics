# the groupby method in Pandas is used to group data based on categorical variables (e.g., drive wheel, body style).

# After grouping, we can apply operations like mean to calculate the average price for each group.

# To make grouped data easier to read, we can convert it into a pivot table, where one variable goes on the rows and the other on the columns.

# A heatmap can then be used to visualize the pivot table, showing data values as colors. This makes it easier to see patterns and relationships (e.g., which drive wheel + body style combination has the highest average price).


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path="file name"
df = pd.read_csv(path)

#1.shoose columns to groupby
df_choose = df[["category 1","category 2","price"]]

#2.excute operation
df_group = df_choose.groupby(["category 1","category 2"]).mean()#the operations on price

#3.implement teble to be easy to read
pivot = df_group.pivot(index="category 1(row)",columns="category 2(column)",values="price")

#4. draw heatmap
plt.pcolor(pivot,cmap="color(coolwarm)")
plt.title("title name")
plt.show()
#OR
sns.heatmap(pivot,annot=True,fmt=.1,cmap="color")
plt.title("title name")
plt.show()