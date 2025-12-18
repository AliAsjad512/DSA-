# df.head()
# df.tail()
# df.info()
# df.describe()
# df.shape
# df.columns
# df.dtypes
import pandas as pd
operators = ['AT&T', 'Verizon', 'T-Mobile US', 'US Cellular']
revenue = [171.76, 128.29, 68.4, 4.04]

#creating a Series from lists
telecom = pd.Series(revenue, index=operators)
telecom

telecom['Verizon']

telecom[[0,2,3]]

# creating the dataframe using dictionary
store_data = pd.DataFrame({'CustomerID': ['CustID00','CustID01','CustID02','CustID03','CustID04']
                           ,'location': ['Chicago', 'Boston', 'Seattle', 'San Francisco', 'Austin']
                           ,'gender': ['M','M','F','M','F']
                           ,'type': ['Electronics','Food&Beverages','Food&Beverages','Medicine','Beauty']
                           ,'quantity':[1,3,4,2,1],'total_bill':[100,75,125,50,80]})

print(store_data['location'])
print(store_data[['location','type','total_bill']])


def profit(s):
    return s + s*0.10 # increase of 10%

data['price'].apply(profit)