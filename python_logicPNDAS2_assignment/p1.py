import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
    "Score": [95, 92, 78, 88, 84, 90, 70],
    "Passed": [True, True, False, True, True, True, False],
    "Category": ["A", "A", "B", "B", "B", "A", "C"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print("\n")

print("Single Column (Score):")
score_column = df["Score"]
print(score_column)
print("\n")

print("Multiple Columns (Name & Score):")
name_score_df = df[["Name", "Score"]]
print(name_score_df)
print("\n")

print("First three rows using iloc:")
print(df.iloc[:3])
print("\n")

df_indexed = df.set_index("Name")

print("Using loc after setting Name as index:")
print(df_indexed.loc[["Alice", "Bob"]])
print("\n")

print("Filtered rows (Score > 85):")
high_scores = df[df["Score"] > 85]
print(high_scores)
print("\n")

print("Filtered rows (Score > 85 AND Passed is True):")
high_passed = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(high_passed)
print("\n")

print("Sorted high-performing students (descending Score):")
sorted_high = high_passed.sort_values("Score", ascending=False)
print(sorted_high)
print("\n")

print("Chained filtering and sorting:")
chained_result = (
    df[(df["Score"] > 85) & (df["Passed"])]
      .sort_values("Score", ascending=False)
)
print(chained_result)