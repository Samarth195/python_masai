import requests
import pandas as pd
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
print(df.head())

df = df.rename(columns = {"userId":"user_id"})
df = df.drop(columns = ["id"])

df["post_length"] = df["body"].apply(len)
print("\nWith Post Length:")
print(df.head())

posts_per_user = df.groupby("user_id").size()
print(posts_per_user)
