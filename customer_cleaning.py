import pandas as pd

data = {
    "customer_id": ["C001", "C002", "C003", "C004", "C002"],
    "name": ["  AMINA JOHNSON ", "Kunle AdeBayo", None,
             "CHIDI OKAFOR", "Kunle AdeBayo"],
    "age": [28, 35, 22, -5, 35],
    "city": ["Lagos", "lagos", "Abuja", "Port Harcourt", "lagos"],
    "email": [
        "amina@example.com",
        "kunle@example.com",
        None,
        "chidi@example.com",
        "kunle@example.com"
    ]
}

df = pd.DataFrame(data)
print(df.shape)
print(df)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df[df.duplicated()])
#standardizing name column
df['name'] = df['name'].str.strip().str.title()
#standardizing city names
df['city'] = df['city'].str.title()
#invalid ages
invalid_age =  (df['age'] < 0) | (df['age'] > 100)
invalid_ages = df['age'][invalid_age]
print(invalid_ages)
#replacing invalid with nan
df.loc[invalid_age, 'age'] = pd.NA
print(df[['customer_id', 'age']])
#missing names
missing_names = df[df['name'].isna()]
print(missing_names)
# missing values across columns
missing_values = df.isna().sum()
print(missing_values)
# missing emails
missing_emails = df[df['email'].isna()]
print(missing_emails)
# removing duplicate rows
df = df.drop_duplicates()
print(df)
print(df.shape)
print(df.isna().sum())
#checking data types
print(df.dtypes)
#converting age column to int64
df['age'] = df['age'].astype('Int64')
print(df.dtypes)
print(df[['customer_id', 'age']])
#saving cleaned data to csv
df.to_csv('cleaned_customers.csv', index=False)

#checking saved csv
check_df = pd.read_csv('cleaned_customers.csv')
print(check_df.shape)
print(check_df.isna().sum())
print(check_df)
