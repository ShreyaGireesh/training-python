import pandas as pd

data = {

'Name': ['John', 'Anna', None, 'Linda', 'Sophia'],

'Age': [28, 24, 40, None, 25],

'Salary': [50000, 55000, 60000, 70000, 65000],

'Join Date': ['2015-03-15', '2017-07-01', '2018-01-12', '2016-08-05', '2019-11-19'],

'Department': ['HR', 'Finance', 'HR', 'IT', 'Finance'],

'Gender': ['Male', 'Female', 'Male', 'Female', 'Female']

}


df = pd.DataFrame(data)
print(df)

print("1. fill missing values in a column with a specific value (e.g., 'Unknown' for Name)\n")
df['Name'].fillna('Unknown')
print(df)

print("2. fill missing numerical values in a column with the mean of that column\n")
df['Age'].fillna(df['Age'].mean())
print(df)

print("3. rows with missing values be removed from a Pandas DataFrame")
df.dropna()
print(df)