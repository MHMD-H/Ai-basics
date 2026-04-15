import pandas as pd
import plotly.express as ex 



file = r"C:\Users\moham_f78sqay\Downloads\students_data.csv"
df = pd.read_csv(file)
print(df)

df_groupy = df.groupby("Level")["Score"].sum().reset_index()
print(df_groupy)

fig = ex.scatter(
    df_groupy,
    x="Level",
    y="Score",
    size="Score", #size of circle
    color="Level",
    hover_name="Score",
    title="Score distribuation",
    size_max=60)
fig.show()