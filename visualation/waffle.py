import pandas as pd 
import matplotlib.pyplot as plt
from pywaffle import Waffle


path = r"C:\Users\moham_f78sqay\Downloads\language_popularity.csv"

df = pd.read_csv(path)

print(df)

fig = plt.figure(
    FigureClass=Waffle,
    rows=15,
    columns = 15,
    values = df,
    colors= ["red","blue","green","black","nevy","purple","grey","dark red","pink","brown"],
    title = {"label" :"The languages distribuation","loc":"center"},
    legend = {"loc":"lower left"}
)
plt.show()