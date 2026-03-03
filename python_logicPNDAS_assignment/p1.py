import pandas as pd

data = {
    "Age":[18, 22, 25, 30, 28, 35, 40, 19, 23, 31],
    "Score": [75, 88, 92, 60, 85, 78, 95, 70, 82, 89],
    "Label":["Pass", "Pass", "Pass", "Fail", "Pass","Pass", "Pass", "Fail", "Pass", "Pass"]
}

df = pd.DataFrame(data)

df.to_csv("Dataset.csv",index = False)
print("CSV file created successfully.")

dataset = pd.read_csv("Dataset.csv")
print("First 5 rows :")
print(dataset.head())
print("\n")

print("Last 5 rows :")
print(dataset.tail())
print("\n")

print("Dataset Information :")
print(dataset.info())
print("\n")

print("Summary Statistics :")
print(dataset.describe())
print("\n")

age_c = dataset["Age"]
print("Selected Column (Age) :")
print(age_c)
print("\n")

selected_c = dataset[["Age","Score"]]
print("Multiple Columns (Age and Score) :")
print(selected_c)
print("\n")

filter_rows = dataset[dataset["Score"]>80]
print("Filtered Rows (Score > 80) :")
print(filter_rows)