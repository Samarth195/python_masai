import pandas as pd
import numpy as np
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}
df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

print("\nMissing Values in Dataset:\n")
print(df.isnull().sum())

df["Salary"].fillna(df["Salary"].mean(), inplace=True)

df.drop(columns=["Temporary_Notes"], inplace=True)

df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

summary = df.groupby("Department")["Annual_Salary"].agg(["mean", "count"])

print("\nFinal Summary Table:\n")
print(summary)