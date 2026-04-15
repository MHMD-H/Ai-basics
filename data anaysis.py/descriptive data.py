# descriptive statistics as a way to explore data(تستكشف الداتا) before building complex models. Using pandas.describe(),
#  you can quickly see key statistics such as mean, count, standard deviation, quartiles, and extremes for numerical variables. Missing values are automatically skipped.

# For categorical variables, you can use value_counts() to summarize frequencies (e.g., how many cars have each type of drive system).

# The video also introduces box plots, which show the distribution of numerical data, including ---> بيوضح بالرسم:

# Median (middle value),

# Upper quartile (75%),

# Lower quartile (25%),

# Interquartile range (IQR),

# Extremes and outliers.(max & min)

# Finally, it covers scatter plots to visualize relationships between two continuous variables(قيميتين متغيرين) (e.g., engine size and price). 
# The predictor variable)(المتغير المستقل) goes on the X-axis,
#  the target variable(المتغير التابع) on the Y-axis. In the example, as engine size increases, car price also increases, showing a positive linear relationship.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path="file name"
df = pd.read_csv(path)

#info about file(man,median)
print(df.describe())

#plot this  information :
#1.matplotlib
plt.figure(figsize(4,8)) # type: ignore
plt.boxplot(df["column name1(x)"],df["column name2(y)"])
plt.title("title name of graph")
plt.xlabel("column name1") #the name of x-axis
plt.ylabel("column name2")#name of y-axis
plt.show()


#2.seaborn -->don't need define axis-labels
sns.boxplot(x=df["column name1(x)"],y=df["column name2(y)"])
plt.title("Boxplot: Price vs Drive Wheel")
plt.show()

#scatter
plt.scatter(df["column name1(x)"],df["column name2(y)"],colorizer="color")
plt.title("title name of graph")
plt.xlabel("column name1") #the name of x-axis
plt.ylabel("column name2")#name of y-axis
plt.show()
