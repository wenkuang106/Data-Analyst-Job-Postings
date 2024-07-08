import pandas as pd

df = pd.read_csv('Datasets\clean.csv')

def split_address(address):
    if "Washington, DC" in address:
        city = "Washington DC"
        state_province = ""
        country = ""
    else:
        parts = address.split(', ')
        city = parts[0]
        state_province = parts[1] if len(parts) > 1 else ""
        country = parts[2] if len(parts) > 2 else ""
    return pd.Series([city, state_province, country])

# Apply the function to the 'full_address' column
df[['city', 'state_province', 'country']] = df['job_location'].apply(split_address)

# View all unique entires within 'country' column 
df.country.unique()

# Confirm 'split_address' function worked properly
df.at[4999, 'city'] = ''
df.at[4999, 'state_province'] = 'Newfoundland and Labrador'
df.at[4999, 'country'] = 'Canada'

# Filter rows where 'full_address' contains "Newfoundland and Labrador"
filtered_df = df[df['country'].str.contains('None', na=False)]
filtered_df = df[df['country'].isna() | (df['country'] == '')]

# Display the filtered DataFrame
print(filtered_df)

# Creating a set containing the all the States,including DC, that are within the US
us_states = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 
    'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 
    'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 
    'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 
    'WI', 'WY', 'Washington DC'
}

# Adding 'United States' to the 'country' column for rows where the 'state_province' and 'city' column
# matches anything listed in the 'us_states' set
df.loc[df['state_province'].isin(us_states), 'country'] = 'United States'
df.loc[df['city'].isin(us_states), 'country'] = 'United States'

countries_to_move = ['United States', 'Canada', 'United Kingdom', 'Mexico', 'Australia']

# Iterate over the DataFrame and update values
for index, row in df.iterrows():
    # Check if state_province or city is in countries_to_move
    if row['state_province'] in countries_to_move:
        df.at[index, 'country'] = row['state_province']
        df.at[index, 'state_province'] = ''
    elif row['city'] in countries_to_move:
        df.at[index, 'country'] = row['city']
        df.at[index, 'city'] = ''

# Create a mapping dictionary for US state abbreviations to full names
us_state_mapping = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas',
    'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware',
    'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 
    'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 
    'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 
    'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 
    'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 
    'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 
    'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Replace the US state abbreviations with their full names
df['state_province'] = df['state_province'].replace(us_state_mapping)

# Save the updated DataFrame back to the same CSV file
#df.to_csv('locations.csv', index=False)

# Display the updated DataFrame
print(df.head())

# Test if everything worked out to the location changes
df.tail(5)
df.loc[4999]
df.loc[69]
df.loc[12750]

df.info()

# df.to_csv('Datasets/cleanedV2.csv', index=False)