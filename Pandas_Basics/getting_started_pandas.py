import pandas as pd


# Basic DataFrames using Pandas
df1 = pd.DataFrame([[2, 4, 6], [10, 20, 30]])
print(df1)

df1 = pd.DataFrame([[2, 4, 6], [10, 20, 30]], columns=['Price', 'Age', 'Value'])
print(df1)

df1 = pd.DataFrame([[2, 4, 6], [10, 20, 30]], columns=['Price', 'Age', 'Value'], index=['First', 'Second'])
print(df1)


df2 = pd.DataFrame([{'Name': 'John', 'LastName': 'Wally'}, {'Name': 'Austin', 'LastName': 'Waldron'}])
print(df2)

get_mean = df1.mean()
print(get_mean)


