import pandas as pd

path = r"C:\Users\moham_f78sqay\Downloads\data.csv"
df = pd.read_csv(path)

print(df.head(5)) #first 5 rows
print('-'*50)
print(df.tail(5)) #last 5 rows
print('-'*50)
print(df.columns) #print the headers
print('-'*50)
print(df["Model"]) #print model's column
print('-'*50)


#df.set_index("Car",inplace=True) #Convert index from nums to column name
#df.index.name = None

df1 = df.replace("BMW","Sold out") #to replace value/ replace(old value , new value)
print(df1)

df = df1.dropna(subset="Car",axis=0) # delete row in cars column if value == NAN  
#axis = 0 --> delete row
#axis = 1 --> delete column

x = df.iloc[:,[0,1]] 
#iloc[row,column]  iloc[row1:row2,[column1,column2]] with index
#loc with labels
print('-'*50)
df.sort_values(by= "Weight",ascending=False,axis=0,inplace=True) #rearrange values
print(df)
print(x)
print(df.dtypes)# define data types (string == object  , int == int64 , float == float64)
print('-'*50)
print(df.info())#define data types & n of columns & n of index & memory usage 
print('-'*50)
print(df.describe())# give a summary of table (count,mean,std,max,min,25%,50%,75%)
print('-'*50)
print(df.describe(include="all"))#give a all info of table (count,mean,std,max,min,25%,50%,75%)
print('-'*50)
print(df[["Volume",'Weight']].describe())# give a summary of volume & wieght (count,mean,std,max,min,25%,50%,75%)
print('-'*50)
print(df['Car'].value_counts())#how much is value is repeated in column
print(df['Car'].value_counts().idxmax())#the most repeated value



df.to_csv(r"C:\Users\moham_f78sqay\Downloads\car2.csv") #save data in this file


#datafreme used to append data 
data = [
    [1, "Mohamed", 18, "A"],
    [2, "Omar", 19, "B"],
    [3, "Sara", 20, "A"]
]

df = pd.DataFrame(data, columns=["ID", "Name", "Age", "Grade"])
#print(df)


# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=['float64', 'int64'])
numeric_df.corr()

df.shape  # -> (200, 5)
df.shape[0]  # -> 200 rows(samples)
df.shape[1]  # -> 5 columns(features)
