import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats as st


path =r"C:\Users\moham_f78sqay\Downloads\sample_100_customers.csv"
df =pd.read_csv(path)
print(df)
print("_"*50)
missing_df=df.isnull()
print("Before edit :")
for column in missing_df.columns.values.tolist() :
    print(missing_df[column].value_counts())
    print("\n")

avg_age =df["Age"].mean()
df["Age"]=df["Age"].fillna(avg_age)

avg_AnnualIncome = df["AnnualIncome"].mean()
df["AnnualIncome"]=df["AnnualIncome"].fillna(avg_AnnualIncome)

min_SpendingScore=df["SpendingScore"].min()
df["SpendingScore"] = df["SpendingScore"].fillna(min_SpendingScore)

missing_df=df.isnull()
print("_"*50)
print("After edit :")
for column in missing_df.columns.values.tolist() :
    print(missing_df[column].value_counts())
    print("\n")

bins_age = [0,25,40,df["Age"].max()]
label_age = ["Young","middle","Old"]
df_bin_Age = pd.cut(df["Age"],bins_age,labels=label_age,include_lowest=True)
print(df_bin_Age)


plt.hist(df_bin_Age,bins=3,edgecolor = "black")
plt.title("Age histogram")
plt.xlabel("Age distribuation")
plt.show()

bins_SpendingScore = np.linspace(df["SpendingScore"].min(),df["SpendingScore"].max(),4)
label_SpendingScore =["LOW","MIDDLE","HIGH"]
df_bin_SpendingScore = pd.cut(df["SpendingScore"],bins_SpendingScore ,labels=label_SpendingScore,include_lowest=True  )
print(df_bin_SpendingScore)
plt.hist(df_bin_SpendingScore,bins=3,edgecolor = "black")
plt.title("scor histogram")
plt.xlabel("score distribuation")
plt.show()


corr_coff,p=st.pearsonr(df["AnnualIncome"],df["SpendingScore"])
print(f"correlation coffient = {corr_coff} \n p_value = {p}")
sns.regplot(x=df["AnnualIncome"],y=df["SpendingScore"])
plt.title("relation between spendscore & income")
plt.xlabel("Income")
plt.ylabel("spend")
plt.show()

sns.heatmap(df[["AnnualIncome","SpendingScore"]].corr(),annot=True,fmt=".1f",cmap="coolwarm")
plt.title("Heat map correlation")
plt.show()
2

df_choose = df[["MembershipLevel","Gender","SpendingScore"]]
df_group = df_choose.groupby(["MembershipLevel","Gender"],as_index=False).mean()
pivot = df_group.pivot(index="Gender",columns="MembershipLevel",values="SpendingScore")
print(pivot)

sns.heatmap(pivot,annot=True,fmt=".1f",cmap="coolwarm")
plt.show()