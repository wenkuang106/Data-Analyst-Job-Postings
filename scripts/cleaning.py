import pandas as pd

df = pd.read_csv('Datasets\postings.csv')

# Handle missing values by dropping rows with missing data
df.dropna(inplace=True)

# Drop unnecessary columns
df = df[['job_title','company','job_location','job level', 'job_type','job_skills']]

# Creating a df that splits the entries 'job_location' into separate columns
split_columns = df['job_location'].str.split(', ', expand=True)

# Ensure the split result has exactly three columns by reindexing
split_columns = split_columns.reindex(columns=[0, 1, 2])

# Assign the split columns to the original DataFrame
df[['city', 'state_province', 'country']] = split_columns

# Resulting dataframe
df.sample()

df.info()

df.to_csv('Datasets/clean.csv', index=False)