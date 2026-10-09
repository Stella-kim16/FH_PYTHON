import numpy as np
import pandas as pd

#Read CSV file and transfer it into DataFrame
file = pd.read_csv("Cars93_missing.csv")

#Transfer object Series into index column of the dataframe
df = pd.DataFrame(data = file)
print(df.head(5))

#Change the data in the column of DataFrame according to
# some condition

df.loc[df["Weight"]<3000, "Weight"] = np.nan
print(df.head(5))

#Get names of the DataFrame columns and sum of losted values DF
print(df.columns)
print(df.isnull().sum())

# Ex-change 2 columns, use function for it. Sort coulumn by name
def exchange_col(df, col1, col2):
    cols = list(df.columns)
    i, j = cols.index(col1), cols.index(col2)
    cols[i],cols[j] = cols[j],cols[i]
    return df[cols]

df = exchange_col(df,"Model", "Price")
df = df.reindex(sorted(df.columns), axis=1)
print(df.head(5))


#Delete upper and lowe 5% in object DataFrame
lower = df["Weight"].quantile(0.05)
upper = df["Weight"].quantile(0.95)

df = df[(df["Weight"] >= lower) & (df["Weight"] <= upper)]

print(df.head(5))

#Replay ( Apply) missed values in the Column with average values.
df["Width"] = df["Width"].fillna(df["Width"].mean())

print(df)

#Create two data frames using the two Dicts, Merge two
#data frames
dict1 = {
    "Name": ["Jessi", "Emma", "Alex"],
    "Age": [20, 24, 23]
}

dict2 = {
    "Score": [100, 95, 80],
    "Grade": ["A", "A", "B"]
}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

# append the second data frame as a new column to the first data frame.
df3 = pd.concat([df1, df2], axis=1)

print(df3)

#For any column create histogram
import matplotlib.pyplot as plt

df["Weight"].hist(bins=10)
plt.xlabel("Weight")
plt.ylabel("Frequency")
plt.title("Weight Histogram")
plt.show()

#Create Correlation Matrix for any column
corr = df.corr(numeric_only=True)

print(corr)