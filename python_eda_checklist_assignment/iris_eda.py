import pandas as pd
import plotly.express as px
 
# loading the iris dataset
df = pd.read_csv("iris.csv")
 
# 1. checking the structure of the dataset
print(df.head())
print(df.shape)
 
# Observation: dataset has 150 rows and 5 columns
# 2. checking column info and missing values
print(df.info())
print(df.isnull().sum())
 
# Observation: no missing values found in the dataset
# 3. checking distribution of petal length
fig = px.histogram(df, x="petal_length", title="Distribution of Petal Length")
fig.show()
 
# Observation: petal length is not evenly distributed, setosa has smaller petal length
# 4. checking for outliers using box plot
fig = px.box(df, y="petal_length", title="Outliers in Petal Length")
fig.show()
 
# Observation: there are a few outliers in petal length
# 5. relationship between petal length and petal width
fig = px.scatter(df, x="petal_length", y="petal_width", color="species", title="Petal Length vs Petal Width")
fig.show()
 
# Observation: petal length and petal width are strongly related, virginica has the largest petal length and width, setosa has the smallest
# 6. comparing species using box plot
fig = px.box(df, x="species", y="petal_length", title="Petal Length by Species")
fig.show()
 