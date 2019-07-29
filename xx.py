import pandas as pd
df = pd.DataFrame(pd.read_csv('./master_data_ready.csv'))
df = df.replace('\N', 'NaN')
print(df)  # 1

df.columns = df.columns.str.capitalize()  # 1
print(df.columns)

Master_Clean = df.drop(['Latitude', 'Longitude'], axis=1)  # 3
#4
print(Master_Clean[(Master_Clean.State == 'NY') & (
    Master_Clean.Post_date > '2018') & (Master_Clean.Post_date < '2019')])

# 5
print(Master_Clean[(Master_Clean.State != 'NY') & (Master_Clean.State != 'CA') & (
    Master_Clean.Salary > 80000) & (Master_Clean.State != 'NaN')])
# 6
median = Master_Clean['Time_to_fill'].median()
print(Master_Clean['Time_to_fill'].replace('NaN', median).head(25))
print(Master_Clean['Time_to_fill'].replace('NaN', median).tail(25))

# 7
print(Master_Clean.dropna().loc[:, [
      'Company', 'Post_date', 'State']][Master_Clean.State == 'NJ'])

# 8
print(Master_Clean.dropna()[Master_Clean.State.isin(
    ['NC', 'PA', 'TX'])].loc[:, ['Company', 'Post_date', 'State']])

# 9
print(Master_Clean.loc[Master_Clean['Region_state'].str.contains(
    'New York|Los Angeles-Long', case=False, na=False), ['City', 'State', 'County', 'Region_state']])

# 10

print(Master_Clean.loc[Master_Clean['Region_state'].str.contains(
    'New York|Seattle', case=False, na=False), [
    'Company', 'Post_date', 'Vertical', 'Salary']][(Master_Clean.Company != 'NaN') & (Master_Clean.Post_date > '2018') & (Master_Clean.Post_date < '2019') & (Master_Clean.Salary > 8000)])

# 11

print('percent: {:.2%}'.format(len(Master_Clean['Salary'] >= 100000)/len(Master_Clean['Salary'])))


# 12
chain = Master_Clean[(Master_Clean.Company == 'Wells Fargo') & (
    (Master_Clean.State == 'NY') | (Master_Clean.State == 'CA'))]


print('percent: {:.2%}'.format(len(chain[chain.Salary>chain['Salary'].mean()])/len(chain)))
