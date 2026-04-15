import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
file = r"C:\Users\moham_f78sqay\Downloads\reviews.csv"

df = pd.read_csv(file)
print(df)
text = '\n'.join(df["Review_Text"])
print(text)

wordcloud = WordCloud(
    width=400,
    height=800,
    background_color="white",
    colormap="viridis"
).generate(text) 
plt.imshow(wordcloud, interpolation='bilinear')  # عرض الصورة بتنعيم
plt.axis("off")  # إخفاء المحاور
plt.show()