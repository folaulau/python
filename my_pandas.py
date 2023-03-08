import pandas as pd

big_array = [{'name':'Folau','age': 20}, {'name':'Lisa','age': 25}]

# Convert the array of dictionaries to a Pandas DataFrame
df = pd.DataFrame(big_array)

# Group the DataFrame by each column and sum the values
tally = df.groupby(df.columns, axis=1).sum()

# Print the tally
print(tally.to_dict())