import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Sophia'],
    'Age': [28, 24, 40, 33, 25],
    'Salary': [50000, 55000, 60000, 70000, 65000],
    'Join Date': ['2015-03-15', '2017-07-01', '2018-01-12', '2016-08-05', '2019-11-19'],
    'Department': ['HR', 'Finance', 'HR', 'IT', 'Finance'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Female']
}

df = pd.DataFrame(data)
print("Original Data")
print(df,"\n", df.info(),"\n")

print("1. Convert a column to a specific format (convert Join Date to datetime format)")
df['Join Date'] = pd.to_datetime(df['Join Date'])
print(df.dtypes, "\n")

print("2. Filter the data where Age > 25")
print(df[df['Age'] > 25], "\n")

print("3. Filter the data where Name is 'Anna'")
print(df[df['Name'] == 'Anna'], "\n")

print("4. Select specific columns (Name and Salary)")
print(df[['Name', 'Salary']], "\n")

print("5. Select first 3 rows")
print(df.head(3), "\n")

print("6. Select rows by index positions using .iloc[]")
print(df.iloc[[1, 3]], "\n")

print("7. Sort the data by Age in ascending order")
print(df.sort_values(by='Age'), "\n")

print("8. Sort the data by Salary in descending order")
print(df.sort_values(by='Salary', ascending=False), "\n")

print("9. Group by Age and calculate the average Salary")
print(df.groupby('Age')['Salary'].mean(), "\n")

print("10. Aggregate multiple statistics (mean, max, min) on Salary by Age")
print(df.groupby('Age')['Salary'].agg(['mean', 'max', 'min']), "\n")

print("11. Apply a function to modify Salary (increase by 10%)")
df['Updated Salary'] = df['Salary'].apply(lambda x: x * 1.10)
print(df, "\n")

print("12. Add a new column for Bonus (5% of Salary)")
df['Bonus'] = df['Salary'] * 0.05
print(df, "\n")

print("13. Rename column Join Date to Joining Date")
df.rename(columns={'Join Date': 'Joining Date'}, inplace=True)
print(df, "\n")

print("14. Drop the Bonus column")
df.drop(columns=['Bonus'], inplace=True)
print(df, "\n")

print("15. Add a new categorical column, Job Role")
df['Job Role'] = ['HR Manager', 'Financial Analyst', 'HR Executive', 'IT Manager', 'Accountant']
print(df, "\n")

print("16. Calculate the average Salary for each department")
print(df.groupby('Department')['Salary'].mean(), "\n")

print("17. Determine which department has the most employees")
print(df['Department'].value_counts().idxmax(), "\n")

print("18. Find which department has the most female employees")
print(df[df['Gender'] == 'Female']['Department'].value_counts().idxmax(), "\n")
