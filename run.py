import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv', encoding='utf-8')
df.fillna('', inplace=True)

# Create the INSERT INTO statement
columns = '`,`'.join(df.columns)
sql_statement = f'INSERT INTO table_name (`{columns}`)\nVALUES'
for row in df.itertuples(index=False, name=None):
    values = ','.join(f'"{v}"' if v != '' else 'NULL' for v in row)
    sql_statement += f'({values}),\n'

# Write the SQL statement to a file
with open('script.sql', 'w', newline='', encoding='utf-8') as file:
    file.write(sql_statement[:-2])
    file.write(';')
