import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("EDA Dashboard")

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
df = df.rename(columns = {"userId":"user_id"})
df = df.drop(columns = ["id"])
df["post_length"] = df["body"].apply(len)

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Posts per User")
posts_per_user = df.groupby("user_id").size().reset_index(name="count")
fig1 = px.bar(
    posts_per_user,
    x="user_id",
    y="count",
    title="Posts per User"
)
st.plotly_chart(fig1)

st.subheader("Post Length Distribution")

fig2 = px.histogram(
    df,
    x="post_length",
    nbins=20,
    title="Distribution of Post Length"
)

st.plotly_chart(fig2)