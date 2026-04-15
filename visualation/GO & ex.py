import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# تحميل البيانات
file = r"C:\Users\moham_f78sqay\Downloads\sample_people_data.csv"
df = pd.read_csv(file)
print(df)

# تقسيم البيانات حسب النوع
male = df[df["Gender"] == "Male"] #new data frame that has only male gender
female = df[df["Gender"] == "Female"]#new data frame that has only female gender

# ------------------------------
# 1️⃣ باستخدام Graph Objects
# ------------------------------

# creating figure
fig1 = go.Figure()


#ploting figure
# الذكور
fig1.add_trace(go.Scatter(
    x=male["Age"], #x axis
    y=male["Height"],#Y axis
    mode="markers",#dots
    name="Male",#legend
    marker=dict(color="blue", size=10)#marker = dict (color = "", size=)
))

# الإناث
fig1.add_trace(go.Scatter(
    x=female["Age"],
    y=female["Height"],
    mode="markers",
    name="Female",
    marker=dict(color="pink", size=10)
))

# العناوين
fig1.update_layout(
    title="Height Distribution",
    xaxis_title="Age",
    yaxis_title="Height"
)

fig1.show()

# ------------------------------
# 2️⃣ باستخدام Plotly Express
# ------------------------------
fig2 = px.scatter(
    df,
    x="Age",
    y="Height",
    color="Gender",
    title="Height Distribution (Plotly Express)"
)

fig2.show()
