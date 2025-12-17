df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.dtypes

operators = ['AT&T', 'Verizon', 'T-Mobile US', 'US Cellular']
revenue = [171.76, 128.29, 68.4, 4.04]

#creating a Series from lists
telecom = pd.Series(revenue, index=operators)
telecom

telecom['Verizon']

telecom[[0,2,3]]